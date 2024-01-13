#!/usr/bin/env python3
"""0. Regex-ing"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function that returns the log message obfuscated,
    use a regex to replace occurrences of certain field values.
    """
    for items in fields:
        message = re.sub(items + "=.+?(?=abc)*\\" + ";", items + "="
                         + redaction + separator, message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Method to filter values in incoming log records """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
