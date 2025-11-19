from flask import Flask, request, jsonify

app = Flask(__name__)

USERS = {"user": "pass"}

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "username and password required"}), 400

    if USERS.get(username) == password:
        return jsonify({"token": "fake-jwt-token-for-" + username}), 200

    return jsonify({"message": "invalid credentials"}), 401


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
