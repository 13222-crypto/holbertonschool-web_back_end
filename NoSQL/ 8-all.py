#!/usr/bin/env python3
"""
Module 8-all
Contains function to list all documents in a PyMongo collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: pymongo collection object
    :return: list of documents, or empty list if collection is empty
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
    
