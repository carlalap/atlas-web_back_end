#!/usr/bin/env python3
""" task. BasicAuth Class
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii


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
