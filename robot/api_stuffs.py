from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/users", methods =["GET"])

def get_users():
    return jsonify([
        {"name": "RandomUser","id" : 1},
        {"name": "user1", "id": 2}
    ])


if __name__ == "__main__":
    app.run(debug =True )