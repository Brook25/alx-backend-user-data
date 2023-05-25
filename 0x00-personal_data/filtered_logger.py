#!/usr/bin/env python3
"""
module for regex-ing
"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    class for redacting formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        init method
        """

        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in a log record
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """function returns log message obfuscated """
    for i in fields:
        message = re.sub(fr'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    function returns logging.Logger object
    """
    obj = logging.getLogger("user_data")
    obj.setLevel(logging.INFO)
    obj.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    obj.addHandler(handler)
    return obj


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function returns a connector to a database"""
    connector = mysql.connector.connect(
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME"))
    return connector


if __name__ == '__main__':
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    query = ("SELECT * FROM users")
    cursor.execute(query)
    for row in cursor:
        string = ""
        for key in row:
            string += "{}={}; ".format(key, row[key])
        print(string)
    cursor.close()
    connection.close()
