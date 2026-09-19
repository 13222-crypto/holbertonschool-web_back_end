#!/usr/bin/env python3
"""
Module 102-log_stats
Provides stats about Nginx logs stored in MongoDB including top 10 IPs.
"""
from pymongo import MongoClient


def log_stats():
    """
    Displays statistics about Nginx logs in the database 'logs',
    collection 'nginx', including top 10 IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Total logs
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # Status check count
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{} status check".format(status_check))

    # Top 10 IPs
    print("IPs:")
    ip_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_collection.aggregate(ip_pipeline)
    for ip in top_ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))


if __name__ == "__main__":
    log_stats()
