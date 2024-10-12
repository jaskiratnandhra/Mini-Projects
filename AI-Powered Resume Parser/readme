# AI-Powered Resume Parser

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green.svg)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-yellow.svg)

An **AI-driven resume parser** that extracts key information such as education, skills, and work experience from resumes using **Natural Language Processing (NLP)**. Parsed data is stored in **MongoDB** for future use, and the process is fully automated using **AWS Lambda** for real-time processing when resumes are uploaded to an **S3** bucket.

## Features
- **Automated Resume Parsing**: Automatically triggers when resumes are uploaded to an S3 bucket.
- **NLP-Powered Parsing**: Uses SpaCy to extract key information like education, skills, and experience from resumes.
- **Real-time Processing**: Integrated with AWS Lambda for real-time resume parsing and data storage in MongoDB.
- **Scalable Design**: Can be expanded to support multiple document formats and custom entity recognition.

## Tech Stack
- **Python**: Core language for building the resume parser and interacting with AWS services.
- **SpaCy**: NLP library to extract entities from resume text.
- **MongoDB**: NoSQL database for storing parsed resume information.
- **AWS Lambda**: Serverless function to automate and process resumes in real time.
- **pdfminer.six**: PDF processing library for extracting text from PDF resumes.
- **Boto3**: AWS SDK for Python to interact with S3.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [AWS Setup](#aws-setup)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Installation

### Prerequisites
- **Python 3.7 or higher**
- **MongoDB**: Set up a local instance or use **MongoDB Atlas**.
- **AWS Account**: Required for AWS Lambda and S3 integration.

### Python Dependencies

Install the required dependencies:

```bash
pip install spacy pdfminer.six boto3 pymongo
```

Download the **SpaCy English language model**:

```bash
python -m spacy download en_core_web_sm
```

### MongoDB Setup

Update the MongoDB connection string in the `lambda_handler.py` file:

```python
client = MongoClient('mongodb://your-mongodb-endpoint:27017/')
```

Ensure that your MongoDB server is running and accessible.

## Project Structure

```bash
├── lambda_handler.py            # AWS Lambda function for resume parsing and data storage
├── mongodb_connection.py        # Helper file for MongoDB connection
├── README.md                    # Project documentation
```

- `lambda_handler.py`: Main Lambda handler to parse resumes and store the information in MongoDB.
- `mongodb_connection.py`: Contains MongoDB connection and data insertion logic.

## Usage

1. **Upload Resume**: Upload a resume (PDF format) to the configured S3 bucket.
2. **Trigger Lambda**: The resume upload triggers the AWS Lambda function (`lambda_handler.py`), which parses the resume using NLP and stores the extracted information (education, skills, experience) in MongoDB.
3. **Access MongoDB**: Access the stored resume data via MongoDB for querying and further use.

### Example MongoDB Document:

```json
{
  "name": "John Doe",
  "education": ["Stanford University"],
  "skills": ["Python", "Machine Learning", "Data Science"],
  "experience": ["Data Scientist at ABC Corp"],
  "file_name": "resume.pdf",
  "source": "S3"
}
```

## AWS Setup

### Step 1: AWS S3

- Create an **S3 bucket** to store resumes.
- Ensure the bucket has permissions to trigger AWS Lambda functions on file uploads.

### Step 2: AWS Lambda

1. **Create Lambda Function**:
   - Go to the AWS Lambda Console.
   - Create a new Lambda function using **Python 3.x**.
   - Upload `lambda_handler.py` as the main function.
   - Ensure the Lambda function has permissions to access S3 and MongoDB.

2. **Set Environment Variables**:
   - Set environment variables in the Lambda console for MongoDB URI and other credentials.

3. **Add S3 Trigger**:
   - Configure an **S3 event trigger** to invoke the Lambda function when a resume is uploaded.

### Step 3: Permissions

Ensure that the Lambda function has appropriate permissions to:
- Read files from S3.
- Connect to MongoDB (if hosted in a secure environment like **MongoDB Atlas**).
- Execute the resume parsing code.

## Future Enhancements

- **Multi-Format Support**: Add support for `.docx` files using the `python-docx` library.
- **Custom NLP Models**: Fine-tune SpaCy models to enhance accuracy in recognizing specific resume fields such as job titles and durations.
- **Error Handling**: Improve error handling for edge cases like unsupported file types or incomplete resume data.
- **Dashboard**: Create a front-end dashboard to upload resumes and view the parsed results in real-time.

