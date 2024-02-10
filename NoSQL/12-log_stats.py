#!/usr/bin/env python3
"""task12. Log stats """

from pymongo import MongoClient


def nginx_logs_stats():
    """Connecting to MongoDB"""
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']

    # Get the total number of documents in the collection
    count_logs = collection.count_documents({})
    print(f"{count_logs} logs")

    # Get the count of logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method} = {count}")

    # Get the count of logs with method=GET and path=/status
    count_status = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{count_status}  status check")


if __name__ == "__main__":
    nginx_logs_stats()
