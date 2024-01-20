#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None

if getenv("AUTH_TYPE") == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif getenv("AUTH_TYPE") == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.before_request
def before_request() -> str:
    """This function is only executed before each
    request that is handled by a function of that blueprint"""
    if auth is None:
        return None

    check_pathlist = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    if not auth.require_auth(request.path, check_pathlist):
        return None

    if (
        not auth.authorization_header(request) and
        not auth.session_cookie(request)
    ):
        abort(401)

    if request.environ.get('current_user') is None:
        abort(403)

    request.environ['current_user'] = auth.current_user(request)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Task1. Error handler: Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ task2. Error handler: Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)