#!/usr/bin/env python3
"""Basic Auth
"""
from .auth import Auth
from base64 import b64decode
import binascii


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
