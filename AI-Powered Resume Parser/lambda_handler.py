
import spacy
import boto3
from pymongo import MongoClient
from pdfminer.high_level import extract_text

# Initialize AWS S3 client and Spacy NLP model
s3 = boto3.client('s3')
nlp = spacy.load('en_core_web_sm')

# MongoDB connection setup
client = MongoClient('mongodb://your-mongodb-endpoint:27017/')
db = client['resume_parser']
collection = db['resumes']

def extract_resume_text(file_path):
    """Extract text from a resume file using pdfminer."""
    return extract_text(file_path)

def parse_resume(text):
    """Use NLP to parse resume details from text."""
    doc = nlp(text)
    education, skills, experience = [], [], []
    
    # Extract relevant entities using SpaCy
    for ent in doc.ents:
        if ent.label_ == 'ORG' and ('University' in ent.text or 'Institute' in ent.text):
            education.append(ent.text)
        elif ent.label_ == 'SKILL':
            skills.append(ent.text)
        elif ent.label_ in ['DATE', 'PERSON', 'ORG']:
            experience.append(ent.text)
    
    return {
        'education': education,
        'skills': skills,
        'experience': experience
    }

def store_resume_data(resume_data):
    """Store parsed resume data in MongoDB."""
    collection.insert_one(resume_data)

def lambda_handler(event, context):
    """Lambda handler that gets triggered on file upload to S3."""
    
    # Extract bucket name and key (file name) from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the resume file from S3
    s3.download_file(bucket, key, '/tmp/resume.pdf')
    
    # Extract resume text
    resume_text = extract_resume_text('/tmp/resume.pdf')
    
    # Parse the resume text
    parsed_resume = parse_resume(resume_text)
    
    # Add metadata (file name, source, etc.)
    parsed_resume['file_name'] = key
    parsed_resume['source'] = 'S3'
    
    # Store the parsed resume data into MongoDB
    store_resume_data(parsed_resume)
    
    return {
        'statusCode': 200,
        'body': 'Resume successfully parsed and stored.'
    }
