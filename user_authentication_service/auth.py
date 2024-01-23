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

    def get_user_from_session_id(self, session_id: str) -> str:
        """Method that find a user by session ID"""
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except Exception:
                return ValueError

    def destroy_session(self, user_id: int) -> None:
        """Method that update the corresponding
        user’s session ID to None"""
        if user_id:
            try:
                self._db.find_user_by(user_id, session_id=None)
            except NoResultFound:
                None

    def get_reset_password_token(self, email: str) -> str:
        """Check if user exist, generate a UUID and update
        the user’s reset_token database field. Return the token.
        """
        if email:
            user = self._db.find_user_by(email=email)
            if email is None:
                raise ValueError
            user.reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=user.reset_token)
            return user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the user's password using the reset token.
        Args:
            reset_token (str): Reset token associated with the user.
            password (str): New password for the user.
        Returns:
            None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            if user:
                password = _hash_password(password)
                self._db.update_user(user.id, hashed_password=password,
                                     reset_token=None)
        except NoResultFound:
            raise ValueError
