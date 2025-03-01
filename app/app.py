from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

conn = psycopg2.connect(database="mydatabase", user="myuser", password="mypassword", host="10.82.66.192", port=8269)

class Account:
    def __init__(self, array):
        self.id = str(array[0])
        self.accountId = str(array[1])
        self.eSignId = str(array[2])
        self.status = str(array[3])
        self.description = str(array[4])
        self.createdAt = str(array[5])
        self.updatedAt = str(array[6])
        self.cert = str(array[7])
        self.tcbsId = str(array[8])
        self.party = str(array[9])
        self.sub = str(array[10])

    def to_dict(self):
        return {
            "id": self.id,
            "accountId": self.accountId,
            "eSignId": self.eSignId,
            "status": self.status,
            "description": self.description,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "cert": self.cert,
            "tcbsId": self.tcbsId,
            "party": self.party,
            "sub": self.sub,
        }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getAccount", methods=['GET'])
def get_account():
    size = int(request.args.get('size', 10))  # default to 10 if not provided
    page = int(request.args.get('page', 1))   # default to 1 if not provided

    # Calculate offset
    offset = (page - 1) * size

    curs = conn.cursor()
    query = "SELECT * FROM ESIGN_ACCOUNT ORDER BY id OFFSET %s ROWS LIMIT %s"
    curs.execute(query, (offset, size))
    accounts = curs.fetchall()
    curs.close()

    account_objects = [Account(account).to_dict() for account in accounts]

    return jsonify(account_objects)

if __name__ == "__main__":
    app.run(debug=True)
