Blockchain-Based Chain of Custody System for Digital Evidence
Overview

Digital investigations require strict handling of evidence to ensure that it remains authentic and unchanged throughout the investigation process. This process is known as the Chain of Custody. Any modification to digital evidence can compromise its reliability in court.

This project demonstrates a prototype system that uses blockchain concepts and cryptographic hashing to maintain the integrity and traceability of digital evidence. The system records evidence handling events in a blockchain-like ledger, making it easier to detect tampering and maintain a transparent history of evidence access.

The goal of this project is to show how blockchain technology can improve security, transparency, and trust in digital forensic investigations.

Features

Upload digital evidence files

Generate SHA-256 hash fingerprints for each file

Store evidence records in a blockchain-style ledger

Maintain a chain of blocks linked using cryptographic hashes

Verify file integrity to detect tampering

Download an evidence log for auditing and documentation

Simple web interface for interacting with the system

How the System Works

Evidence Upload
The investigator uploads a digital evidence file through the web interface.

Hash Generation
The system generates a SHA-256 hash of the file.
This hash acts as a unique fingerprint of the evidence.

Blockchain Record Creation
A new block is created containing:

Case ID

Evidence file name

Investigator / Evidence Handler

Timestamp

SHA-256 hash

Previous block hash

Blockchain Linking
Each block is linked to the previous block using its hash value.
This ensures that any modification to earlier records can be detected.

Evidence Verification
When evidence is uploaded again for verification, the system recomputes the hash and compares it with stored records to determine whether the evidence has been modified.

Technologies Used

Python

Flask Web Framework

SHA-256 Cryptographic Hashing

HTML / CSS

Gunicorn (Production server)

Render Cloud Platform (Deployment)

System Architecture
User Interface (Flask Web App)
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
Integrity Verification System
        │
        ▼
Evidence Log Export (CSV)
Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/evidence-blockchain.git
cd evidence-blockchain
2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py

Open in browser:

http://localhost:5000
Deployment

This project can be deployed on platforms such as:

Render

Heroku

Railway

AWS

For this project, deployment was performed using Render, which hosts the Flask application and provides a public URL for access.

Example Workflow

Investigator uploads evidence file

System generates SHA-256 hash

A new block is added to the blockchain ledger

Evidence integrity can be verified later

Evidence log can be exported for investigation records

Future Improvements

Smart contract integration with Ethereum

Decentralized blockchain nodes

Database storage for persistent blockchain records

Role-based user authentication

Enhanced visualization of blockchain transactions

Author

Project developed as part of an academic study on blockchain applications in digital forensics.
