#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB:
"""
from pymongo import MongoClient


def log_stats(collection):
    """Print stats about the Nginx logs stored in the given collection."""
    print(f"{collection.count_documents({})} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"\tmethod {method}: "
              f"{collection.count_documents({'method': method})}")
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


log_stats(MongoClient("mongodb://127.0.0.1:27017").logs.nginx)