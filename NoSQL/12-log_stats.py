#!/usr/bin/env python3
"""task12. Log stats """

from pymongo import MongoClient


def nginx_logs_stats():
    """Connecting to MongoDB"""
    client = MongoClient('localhost', 27017)
    db = client.logs.nginx

    # Get the total number of documents in the collection
    count_logs = db.count_documents({})
    print(f"{count_logs} logs")

    # Get the count of logs for each method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = db.count_documents({"method": method})
        print(f"\tmethod {method} = {count}")

    # Get the count of logs with method=GET and path=/status
    count_status = db.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{count_status}  status check")


if __name__ == "__main__":
    nginx_logs_stats()
