
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb://your-mongodb-endpoint:27017/')
db = client['resume_parser']
collection = db['resumes']

def store_resume_data(resume_data):
    """Store parsed resume data in MongoDB."""
    collection.insert_one(resume_data)
