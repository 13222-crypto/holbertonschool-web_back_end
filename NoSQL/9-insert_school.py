#!/usr/bin/env python3
"""
Module 9-insert_school
Contains function to insert a new document into a PyMongo collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    :param mongo_collection: pymongo collection object
    :param kwargs: key-value pairs representing the document fields
    :return: the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
