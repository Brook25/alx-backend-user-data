#!/usr/bin/env python3
"""
modul contains Auth class
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """
    class Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        method require_auth
        """
        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        has_wildcard = any(x.endswith("*") for x in excluded_paths)
        if not has_wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if e.endswith("*"):
                if path.startswith(e[:-1]):
                    return False
            if path == e:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        method authorization_header
        """
        if request:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        method curent_user
        """
        return None

    def session_cookie(self, request=None):
        """
        method session_cookie
        """
        if request is None:
            return None

        _my_session_id = os.getenv('SESSION_NAME')
        res = request.cookies.get(_my_session_id)

        return res
