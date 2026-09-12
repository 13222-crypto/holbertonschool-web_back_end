#!/usr/bin/env python3
"""
Module for MongoDB insertion operations using PyMongo.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Args:
        mongo_collection: PyMongo collection object.
        **kwargs: Key-value pairs representing the document.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
