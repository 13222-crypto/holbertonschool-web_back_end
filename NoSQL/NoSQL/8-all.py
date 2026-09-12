#!/usr/bin/env python3
"""
Module for MongoDB listing operations using PyMongo.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    return list(mongo_collection.find())
