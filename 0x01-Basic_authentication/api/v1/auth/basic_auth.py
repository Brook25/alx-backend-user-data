#!/usr/bin/env python3
"""Basic Auth
"""
from .auth import Auth
from base64 import b64decode
import binascii
from typing import TypeVar
from api.v1.views.users import User


class BasicAuth(Auth):
    """Class for Basic Authentication"""
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """returns the authentication token"""
        if authorization_header and type(authorization_header) is str:
            if authorization_header[:6] == 'Basic ':
                return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """Decodes the base64 encoded Authorization header value"""
        b64_auth = base64_authorization_header
        if b64_auth and type(b64_auth) is str:
            try:
                return b64decode(b64_auth).decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Returns user email and password from the decoded value"""
        decoded = decoded_base64_authorization_header
        if decoded and type(decoded) is str and ':' in decoded:
            return tuple(decoded.split(':'))
        return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Validates user email and password"""
        if user_email and user_pwd:
            if type(user_email) is str and type(user_pwd) is str:
                for user in User.search():
                    if user.email == user_email:
                        if user.is_valid_password(user_pwd):
                            return user
