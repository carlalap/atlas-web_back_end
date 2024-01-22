from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth
from api.v1.views import app_views

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """ Handle Session authentication login """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user[0].id)
    user_data = user[0].to_json()

    response = jsonify(user_data)
    response.set_cookie(
        auth.SESSION_NAME,
        session_id,
        httponly=True,
        secure=True if app_views.app.config['ENV'] == 'production' else False
    )

    return response
