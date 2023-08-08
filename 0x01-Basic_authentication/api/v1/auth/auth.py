#!/usr/bin/env python3
"""AUTH class
"""
from typing import List, TypeVar
from flask import request
from api.v1.views.users import User

class Auth:
    """template class for authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authorizaition for a certain path"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """get authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets current user"""
        return None
