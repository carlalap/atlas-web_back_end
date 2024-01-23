#!/usr/bin/env python3
"""Flask app
with a single GET route ("/") that returns
a JSON payload using flask.jsonify:"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def welcome():
    """Return a Welcome message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Method implement the end-point to register a user."""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login function to respond to the POST /sessions"""
    email = request.form.get('email')
    password = request.form.get('password')
    # Check if login credentials are valid using Auth.valid_login
    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """function to respond to the DELETE /sessions route, Log Out!.
        request is expected to contain the session
        ID as a cookie with key "session_id"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user)
    return redirect(302)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """function to respond to the GET /profile route."""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200

    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
