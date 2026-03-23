import hashlib
import datetime
import os

from flask import Flask, request, render_template, redirect

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


class Block:
    def __init__(self, index, timestamp, evidence_name, evidence_hash,
                 from_person, to_person, previous_hash):

        self.index = index
        self.timestamp = timestamp
        self.evidence_name = evidence_name
        self.evidence_hash = evidence_hash
        self.from_person = from_person
        self.to_person = to_person
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.index}{self.timestamp}{self.evidence_name}{self.evidence_hash}{self.from_person}{self.to_person}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:

    def __init__(self):
        self.chains = {}
        self.chain_counter = 1

    def start_chain(self, evidence_name, evidence_hash, investigator):

        chain_id = self.chain_counter
        self.chain_counter += 1

        genesis = Block(
            0,
            str(datetime.datetime.now()),
            evidence_name,
            evidence_hash,
            "SYSTEM",
            investigator,
            "0"
        )

        self.chains[chain_id] = {
            "blocks": [genesis],
            "closed": False
        }

    def transfer(self, chain_id, from_person, to_person):

        chain = self.chains[chain_id]["blocks"]

        prev = chain[-1]

        block = Block(
            len(chain),
            str(datetime.datetime.now()),
            prev.evidence_name,
            prev.evidence_hash,
            from_person,
            to_person,
            prev.hash
        )

        chain.append(block)

    def close_chain(self, chain_id):
        self.chains[chain_id]["closed"] = True


blockchain = Blockchain()


def hash_file(filepath):

    sha = hashlib.sha256()

    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sha.update(chunk)

    return sha.hexdigest()


@app.route("/")
def index():
    return render_template("index.html", chains=blockchain.chains)


@app.route("/start", methods=["POST"])
def start():

    file = request.files["file"]
    investigator = request.form["investigator"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    file_hash = hash_file(filepath)

    blockchain.start_chain(file.filename, file_hash, investigator)

    return redirect("/")


@app.route("/transfer", methods=["POST"])
def transfer():

    chain_id = int(request.form["chain_id"])
    from_person = request.form["from_person"]
    to_person = request.form["to_person"]

    blockchain.transfer(chain_id, from_person, to_person)

    return redirect("/")
    
@app.route("/verify", methods=["POST"])
def verify():

    file = request.files["verifyfile"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    new_hash = hash_file(filepath)

    for chain in blockchain.chains.values():
        for block in chain["blocks"]:

            if block.evidence_hash == new_hash:
                return "<h3 style='color:green'>✔ Evidence VERIFIED - Integrity intact</h3>"

    return "<h3 style='color:red'>⚠ Evidence NOT FOUND in blockchain</h3>"    


@app.route("/close", methods=["POST"])
def close():

    chain_id = int(request.form["chain_id"])

    blockchain.close_chain(chain_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
