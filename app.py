import hashlib
import datetime
import os
import csv

from flask import Flask, request, render_template, redirect, send_file

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    file_hash = hash_file(filepath)

    blockchain.add_block(file.filename, file_hash, investigator)

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
