Blockchain-Based Chain of Custody System for Digital Evidence






Overview

Digital investigations require strict handling of evidence to ensure that it remains authentic and unchanged from the time it is collected until it is presented in court. This process is known as the Chain of Custody.

This project demonstrates a prototype Blockchain-Based Chain of Custody System that records evidence handling events using blockchain concepts and SHA-256 cryptographic hashing. The system provides a tamper-evident ledger for tracking digital evidence.

Features

Upload digital evidence files

Generate SHA-256 cryptographic hash fingerprints

Store records in a blockchain-style ledger

Maintain a tamper-evident chain of evidence blocks

Verify file integrity

Download evidence logs for auditing

Web interface for investigators

How the System Works

Evidence Upload
The investigator uploads a digital evidence file.

Hash Generation
The system generates a SHA-256 hash, which acts as a unique fingerprint of the file.

Block Creation

Each block stores the following information:

Case ID

Evidence file name

Evidence handler

Timestamp

File hash

Previous block hash

Blockchain Linking

Each block references the hash of the previous block, creating a linked chain of blocks.

Evidence Verification

To verify evidence integrity, the system recomputes the file hash and compares it with the stored hash.

System Architecture
User Interface (Flask)
        │
        ▼
Evidence Upload Module
        │
        ▼
SHA-256 Hash Generation
        │
        ▼
Blockchain Ledger (Linked Blocks)
        │
        ▼
Evidence Integrity Verification
Technologies Used
Technology	Purpose
Python	Core programming language
Flask	Web application framework
SHA-256	Cryptographic hashing for file integrity
HTML / CSS	User interface
Gunicorn	Production server
Render	Cloud deployment
Project Structure
evidence-blockchain
│
├── app.py
├── requirements.txt
├── blockchain.json
├── uploads/
│
└── templates
    └── index.html
Installation
Clone the Repository
git clone https://github.com/YOUR_USERNAME/evidence-blockchain.git
cd evidence-blockchain
Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py

Open your browser and visit:

http://localhost:5000
Deployment

This application can be deployed using platforms such as:

Render

Heroku

Railway

AWS

For this project, deployment was performed using Render, which hosts the Flask application and provides a public URL.

Example Workflow

Upload digital evidence

System generates SHA-256 fingerprint

Blockchain block is created

Evidence integrity can be verified

Evidence logs can be downloaded

Future Improvements

Smart contract integration with Ethereum

Decentralized blockchain nodes

Persistent database storage

User authentication system

Blockchain visualization dashboard

Author

Academic project exploring blockchain applications in digital forensics and digital evidence management.
