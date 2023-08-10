#!/usr/bin/env python3
"""Session Auth
"""
from .auth import Auth
from uuid import uuid4
import os
from models.user import User


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
        """returns cookie value based on a session name"""
        if request:
            return request.cookies.get(os.getenv('SESSION_NAME'))

    def current_user(self, request=None):
        """retrieve current user instance"""
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_id = self.user_id_for_session_id(session_id)
                if user_id:
                    return User.get(user_id)

    def destroy_session(self, request=None):
        """"""
        if request:
            session_id = self.session_cookie(request)
            if session_id and self.user_id_for_session_id(session_id):
                del self.user_id_by_session_id[session_id]
                return True
        return False
