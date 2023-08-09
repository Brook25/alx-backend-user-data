#!/usr/bin/env python3
"""AUTH class
"""
from typing import List, TypeVar
from flask import request
from api.v1.views.users import User
import os
import re


class Auth:
    """template class for authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authorizaition for a certain path"""
        path = path + '/' if path and path[-1] != '/' else path
        if not (path and excluded_paths):
            return True
        for exc_path in excluded_paths:
            if bool(re.match(exc_path.replace('*', '.*'), path)):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """get authorization header"""
        if request and 'Authorization' in request.headers:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current user"""
        return None

    def session_cookie(self, request=None):
        """returns session cookie value"""
        if request:
            return request.cookies.get(os.getenv('SESSION_NAME'))
