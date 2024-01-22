#!/usr/bin/env python3
"""
Auth Module
"""
import bcrypt
from db import DB
from uuid import uuid4
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Method that takes in a password string
    arguments and returns bytes."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generate a random uuid """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that register a new user
        take mandatory email and password
        string arguments and return a User object."""
        try:
            reg_user = self._db.find_user_by(email=email)
        except NoResultFound:
            passw = _hash_password(password)
            reg_user = self._db.add_user(email, passw)
            return reg_user
        else:
            raise ValueError('User {} already exists'.format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Method that check login using email and checking the
        password bcrypt.checkpw """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Method that find the user corresponding
        to the email, generate a new UUID and store
        it in the database as the user’s session_id,
        then return the session ID."""
        user = self._db.find_user_by(email=email)
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
