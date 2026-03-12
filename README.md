Blockchain-Based Chain of Custody System for Digital Evidence








Overview

Digital investigations rely heavily on the chain of custody, which ensures that evidence remains authentic and unaltered from the moment it is collected until it is presented in court.

This project demonstrates a Blockchain-Based Chain of Custody System for Digital Evidence. The system records evidence handling events in a blockchain-style ledger and uses SHA-256 cryptographic hashing to detect any tampering with digital files.

By combining blockchain principles with a simple web interface, the system provides a transparent and tamper-evident method for managing digital forensic evidence.

Key Features

• Upload digital evidence files
• Generate SHA-256 hash fingerprints
• Store records in a linked blockchain ledger
• Maintain tamper-evident evidence history
• Verify file integrity
• Download evidence logs for auditing
• Simple web interface for investigators

How the System Works

The system simulates blockchain behaviour to track digital evidence.
Evidence Upload
      │
      ▼
SHA-256 Hash Generation
      │
      ▼
Blockchain Block Creation
      │
      ▼
Linked Block Storage
      │
      ▼
Integrity Verification

Step-by-step process

Investigator uploads an evidence file.

The system generates a SHA-256 hash for the file.

A new block is created containing:

Case ID

Evidence file name

Evidence handler

Timestamp

File hash

Previous block hash

The block is appended to the blockchain ledger.

Evidence can later be verified by recomputing the file hash and comparing it with the stored record.


+----------------------------+
|        Web Interface       |
|         (Flask)            |
+-------------+--------------+
              |
              ▼
+----------------------------+
|   Evidence Upload Module   |
+-------------+--------------+
              |
              ▼
+----------------------------+
| SHA-256 Hash Generation    |
+-------------+--------------+
              |
              ▼
+----------------------------+
| Blockchain Ledger Storage  |
| (Linked Blocks Structure)  |
+-------------+--------------+
              |
              ▼
+----------------------------+
| Evidence Integrity Check   |
+----------------------------+


Technologies Used
Technology	Purpose
Python	Core programming language
Flask	Web application framework
SHA-256	Cryptographic hashing for evidence integrity
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
Clone the repository
git clone https://github.com/YOUR_USERNAME/evidence-blockchain.git
cd evidence-blockchain
Create virtual environment
python3 -m venv venv
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run the application
python app.py

Open your browser:

http://localhost:5000
Deployment

The application can be deployed using cloud platforms such as:

Render

Heroku

Railway

AWS

For this project, deployment was performed using Render, allowing the application to run as an online web service.

Example Use Case

Investigator uploads a digital evidence file.

The system generates a SHA-256 fingerprint.

A blockchain block is created with evidence metadata.

The evidence record becomes part of the tamper-evident ledger.

Evidence integrity can later be verified during investigation or court proceedings.

Future Improvements

Possible enhancements for future versions include:

• Integration with Ethereum smart contracts
• Decentralized blockchain nodes
• Persistent database storage
• User authentication and role management
• Improved blockchain visualization

Author

Developed as part of an academic project exploring the use of blockchain technology in digital forensics and evidence management.
