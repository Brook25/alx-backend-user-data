#!/usr/bin/env python3
"""Persist User session in a file
"""
from .base import Base


class UserSession(Base):
   """Session class to persist sessions in DB""" 
    def __init__(self, *args: list, **kwargs: dict):
        """Init an object"""
        super().__init__(kwargs)
        if args:
            self.user_id = args[0]
            self.id = args[1]
        else:
            self.user_id = kwargs.get('user_id')
            self.id = kwargs.get('id')
