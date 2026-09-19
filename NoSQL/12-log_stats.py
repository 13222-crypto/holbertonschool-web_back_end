#!/usr/bin/env python3
"""
Module 12-log_stats
Provides stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays statistics about Nginx logs in the database 'logs',
    collection 'nginx'.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total logs count
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check count (GET method with path /status)
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))


if __name__ == "__main__":
    log_stats()
