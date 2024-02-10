#!/usr/bin/env python3
"""task9. Insert a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a
    collection based on kwargs"""
    new_data = mongo_collection.insert_one(kwargs)
    # Return the new _id
    return new_data.inserted_id
