#!/usr/bin/env python3
"""task5. Encrypting passwords &
task6. Check valid password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Function that expects one string argument
    name password and returns a salted, hashed password,
    which is a byte string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function that expects 2 arguments (hashed_password & password)
    and returns a boolean"""
    encoded_passw = bytes(password, 'utf-8')
    if bcrypt.checkpw(encoded_passw, hashed_password) is True:
        return True
    else:
        return False
