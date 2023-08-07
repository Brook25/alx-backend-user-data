#!/usr/bin/env python3
from filtered_logger import get_db, get_logger, PII_FIELDS
import re

FIELDS = PII_FIELDS + ('ip', 'last_login', 'user_agent')

logger = get_logger()
connection = get_db()
cursor = connection.cursor()
cursor.execute('SELECT * FROM users')
for row in cursor:
    row = list(row)
    row[6] = row[6].strftime('%Y-%m-%d %H:%M:%S')
    message = list(zip(FIELDS, row))
    message = ['='.join(field) for field in message]
    message = '; '.join(message)
    logger.info(message)
cursor.close()
connection.close()
