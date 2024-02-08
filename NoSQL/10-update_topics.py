#!/usr/bin/env python3
"""task10. Change school topics """

from typing import List


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a
    school document based on the name"""
    updated_document = mongo_collection.update_many({"name": name},
                                         {"$set": {"topics": topics}})
    return updated_document.modified_count
