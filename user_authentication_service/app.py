#!/usr/bin/env python3
"""Flask app
with a single GET route ("/") that returns
a JSON payload using flask.jsonify:"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth
app = Flask(__name__)


AUTH = Auth()


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
        return jsonify({"error": "Invalid session ID"}), 403

    AUTH.destroy_session(user)
    return redirect(url_for('/'))


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """function to respond to the GET /profile route."""
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200

    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """Method to respond to the resetpond to the POST /reset_password
    """
    try:
        email = request.form.get('email')
        if email:
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Update the password. If the token is invalid, catch the exception and
    respond with a 403 HTTP code.
    Args:
        "email", "reset_token" and "new_password"
    Return:
        None
    """
    email = request.form.get('email')
    new_pwd = request.form.get('new_password')
    token = request.form.get('reset_token')
    try:
        AUTH.update_password(token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
