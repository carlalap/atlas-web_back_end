#!/usr/bin/env python3
"""0. Regex-ing"""
import re
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
