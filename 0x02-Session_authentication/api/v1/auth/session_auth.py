#!/usr/bin/env python3
"""Session Auth
"""
from .auth import Auth
from uuid import uuid4
import os


class SessionAuth(Auth):
    """Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session ID"""
        if user_id and type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user_id based on session_id """
        if session_id and type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def session_cookie(self, request=None):
        """"""
        if request:
            return request.cookies.get(os.getenv('SESSION_NAME'))
