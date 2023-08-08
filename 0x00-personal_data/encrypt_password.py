#!/usr/bin/env python3
"""password encryption function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a hashed password"""
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd, salt)
    return hashed_pwd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates if two passwords match"""
    hashed_password_2 = password.encode('utf-8')
    return bcrypt.checkpw(hashed_password_2, hashed_password)
