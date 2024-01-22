#!/usr/bin/env python3
"""Flask app
with a single GET route ("/") that returns
a JSON payload using flask.jsonify:"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def welcome():
    """Return a Welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/user', methods=['POST'], strict_slashes=False)
def users() -> str:
    """Method implement the end-point to register a user."""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
