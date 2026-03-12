import hashlib
import datetime
import os
import csv
import json

from flask import Flask, request, render_template, redirect, send_file

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


class Block:
    def __init__(self, index, timestamp, evidence_name, evidence_hash, investigator, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.evidence_name = evidence_name
        self.evidence_hash = evidence_hash
        self.investigator = investigator
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.evidence_name}{self.evidence_hash}{self.investigator}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    BLOCKCHAIN_FILE = "blockchain.json"

def save_blockchain(chain):
    data = []
    for block in chain:
        data.append(block.__dict__)
    with open(BLOCKCHAIN_FILE, "w") as f:
        json.dump(data, f)

def load_blockchain():
    if not os.path.exists(BLOCKCHAIN_FILE):
        return None
    with open(BLOCKCHAIN_FILE, "r") as f:
        data = json.load(f)
    chain = []
    for b in data:
        block = Block(
            b["index"],
            b["timestamp"],
            b["evidence_name"],
            b["evidence_hash"],
            b["investigator"],
            b["previous_hash"]
        )
        chain.append(block)
    return chain
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis", "0", "System", "0")

    def add_block(self, evidence_name, evidence_hash, investigator):
        prev = self.chain[-1]
        block = Block(
            len(self.chain),
            str(datetime.datetime.now()),
            evidence_name,
            evidence_hash,
            investigator,
            prev.hash
        )
        self.chain.append(block)


blockchain = Blockchain()
saved_chain = load_blockchain()
if saved_chain:
    blockchain.chain = saved_chain


def hash_file(filepath):
    sha = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)

    return sha.hexdigest()


@app.route("/")
def index():
    return render_template("index.html", chain=blockchain.chain)


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]
    investigator = request.form["investigator"]
    case_id = request.form["caseid"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    file_hash = hash_file(filepath)

blockchain.add_block(f"{case_id} - {file.filename}", file_hash, investigator)
save_blockchain(blockchain.chain)

    return redirect("/")


@app.route("/verify", methods=["POST"])
def verify():

    file = request.files["verifyfile"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    new_hash = hash_file(filepath)

    for block in blockchain.chain:
        if block.evidence_hash == new_hash:
            return "<h3 style='color:green'>✔ Evidence VERIFIED - Integrity intact</h3>"

    return "<h3 style='color:red'>⚠ WARNING: Evidence hash mismatch - Possible tampering detected</h3>"


@app.route("/download")
def download():

    filename = "evidence_log.csv"

    with open(filename, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["Index", "Timestamp", "Evidence", "Hash", "Investigator", "Previous Hash"])

        for block in blockchain.chain:
            writer.writerow([
                block.index,
                block.timestamp,
                block.evidence_name,
                block.evidence_hash,
                block.investigator,
                block.previous_hash
            ])

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
