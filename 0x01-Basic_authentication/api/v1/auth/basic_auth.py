#!/usr/bin/env python3
"""Basic Auth
"""
from auth import Auth


class BasicAuth(Auth):
    """Class for Basic Authentication"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """returns the authentication token"""
        if authorization_header and type(authorization_header) is str:
            if authorization_header[:6] == 'Basic ':
                return authorization_header[6:]
