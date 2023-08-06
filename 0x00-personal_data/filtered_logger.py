#!/usr/bin/env python3
"""Filtered logger
"""
import re
from typing import List

def filter_datum(fields: List, redaction: str, message: str, separator: str) -> str:
    """returns an obfuscated version of the log message"""
    for field in fields:
        message = re.sub(f"{field}(.+?){separator}", f"{field}={redaction}{separator}", message)
    return message
