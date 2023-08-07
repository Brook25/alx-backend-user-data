#!/usr/bin/env python3
"""password encryption function
"""
import bcrypt


def hash_password(password):
    """returns a hashed password"""
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd, salt)
    return hashed_pwd
