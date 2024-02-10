#!/usr/bin/env python3
"""task10. Change school topics """


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a
    school document based on the name"""
    output = mongo_collection.update_one({"name": name},
                                         {"$set": {"topics": topics}})
    return output.modified_count
