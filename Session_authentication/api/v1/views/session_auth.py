#!/usr/bin/env python3
"""Flask view that handles all
routes for the Session authentication."""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """Method that handle session authentication login
    with the person email and password"""
    email_per = request.form.get('email')
    if not email_per:
        return jsonify({"error": "email missing"}), 400
    password_per = request.form.get('password')
    if not password_per:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email_per})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password_per):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            users_json = jsonify(user.to_json())
            users_json.set_cookie(getenv('SESSION_NAME'), session_id)
            return users_json
        else:
            return jsonify({"error": "wrong password"}), 401
