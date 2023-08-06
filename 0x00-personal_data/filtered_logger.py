#!/usr/bin/env python3
"""Filtered logger
"""
import re

def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """returns an obfuscated version of the log message"""
    for field in fields:
        message = re.sub(f"{field}(.+?){separator}", f"{field}={redaction}{separator}", message)
    return message
