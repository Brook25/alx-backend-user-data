#!/usr/bin/env python3
"""Filtered logger
"""
import csv
import mysql.connector as connector
import re
from typing import List, Tuple, Iterator
import logging
import os

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns an obfuscated version of the log message"""
    for field in fields:
        message = re.sub(f"{field}(.+?){separator}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initalize instance"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """calls super.format() on redacted message"""
        record.msg = filter_datum(self.__fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """func returns a custom logger"""
    global PII_FIELDS
    logger = logging.getLogger('user_data')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> connector.connection.MySQLConnection:
    """returns a mysql connection"""
    connection = connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''),
        database=os.environ.get('PERSONAL_DATA_DB_NAME')
    )
    return connection
