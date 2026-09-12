#!/usr/bin/env python3
"""
Module for MongoDB listing operations using PyMongo.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        List of documents or an empty list if none exist.
    """
    return list(mongo_collection.find())
