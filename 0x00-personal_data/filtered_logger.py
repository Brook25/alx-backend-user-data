#!/usr/bin/env python3
"""Filtered logger
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns an obfuscated version of the log message"""
    for field in fields:
        message = re.sub(f"{field}(.+?);", f"{field}={redaction};", message)
    return message
