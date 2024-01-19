#!/usr/bin/env python3
""" task. BasicAuth Class
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from models.user import User
from typing import TypeVar, List


class BasicAuth(Auth):
    """ BasicAuthenticacion class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract_base65 returns the Base64 part of the Authorization
        header for a Basic Authentication:"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method that returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            decoded_bytes = b64decode(base64_authorization_header)
        except binascii.Error as err:
            return None

        return decoded_bytes.decode("utf-8")

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """method that returns the user email and password
        from the Base64 decoded value"""
        if (
            decoded_base64_authorization_header is None or not
            isinstance(decoded_base64_authorization_header, str)
        ):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Method that return the User instance based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})

        if not users:
            return None

        user_instance = users[0]

        if not user_instance.is_valid_password(user_pwd):
            return None

        return user_instance

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that overloads Auth and retrieves the User
        instance for a request"""
        if request is None:
            request = request

        auth_header = self.authorization_header(request)
        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        user_email, user_pwd = self.extract_user_credentials(
            decoded_auth_header)

        return self.user_object_from_credentials(user_email, user_pwd)
