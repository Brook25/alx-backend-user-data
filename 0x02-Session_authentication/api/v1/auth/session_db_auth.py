#!/usr/bin/env python3
"""Session data base Authentication
"""
from .session_exp_auth import SessionExpAuth
import os
from uuid import uuid4
from datetime import timedelta, datetime
from models.user_session import UserSession
#from models.base import TIMESTAMP_FORMAT
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"


class SessionDBAuth(SessionExpAuth):
    """Session persisted in db and expired accoring
    to expiry time
    """
    def create_session(self, user_id=None):
        """Creates Session"""
        session = UserSession(user_id, str(uuid4()))
        session.save()
        return session.id

    def user_id_for_session_id(self, session_id=None):
        """Retrieves user_id for session_id"""
        if session_id:
            session = UserSession.search({'id': session_id})[0]
            if session:
                if session.created_at + timedelta(seconds=self.session_duration) > datetime.now():
                    return session.user_id
    
    def destroy_session(self, request=None):
        """Destroy session during logout"""
        if request:
            session_id = request.cookies.get(os.getenv('SESSION_NAME'))
            session = UserSession.search({'id': session_id})[0]
            session.remove()
