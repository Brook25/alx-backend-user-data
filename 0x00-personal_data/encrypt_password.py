#!/usr/bin/env python3
"""
module contains funcs to Encrypt Passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function returns a salted, hashed password,
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function validates that the provided password matches
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
