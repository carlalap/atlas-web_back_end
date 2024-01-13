#!/usr/bin/env python3
"""Tasks: 0.Regex-ing, 1.Log formatter, 2.Create logger,
3.Connect to secure database, 4.Read and filter data"""
import re
import logging
import os
import mysql.connector
from typing import List


"""containing the fields from user_data.csv that are considered PII."""
PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


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


def get_logger() -> logging.Logger:
    """function that takes no arguments
    and returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(RedactingFormatter(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function that returns a connector to the database
    (mysql.connector.connection.MySQLConnection object)."""
    return mysql.connector.connect(
        database=os.environ.get("PERSONAL_DATA_DB_NAME", "root"),
        host=os.environ.get("PERSONAL_DATA_DB_HOST", "localhots"),
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD"),
    )
