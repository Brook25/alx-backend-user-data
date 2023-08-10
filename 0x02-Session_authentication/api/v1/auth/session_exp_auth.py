#!/usr/bin/env python3
"""Session Auth with expiry
"""
from .session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Class sets expiry to session id"""

    def __init__(self):
        """Inits session auth with expiration"""
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except TypeError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create session with a created at value"""
        session_id = super().create_session(user_id)
        if session_id:
            session = {'user_id': user_id, 'created_at': datetime.now()}
            self.user_id_by_session_id[session_id] = session
            return session_id

    def user_id_for_session_id(self, session_id=None):
        """return user id based on expiry of session"""
        if session_id:
            session = self.user_id_by_session_id.get(session_id)
            if session:
                if self.session_duration <= 0:
                    return session.get('user_id')
                if 'created_at' in session:
                    duration = timedelta(seconds=self.session_duration)
                    if session.get('created_at') + duration > datetime.now():
                        return session.get('user_id')
