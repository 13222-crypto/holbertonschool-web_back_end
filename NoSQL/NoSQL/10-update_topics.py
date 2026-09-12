#!/usr/bin/env python3
"""
Module for MongoDB update operations using PyMongo.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name.

    Args:
        mongo_collection: PyMongo collection object.
        name (str): School name to match.
        topics (list): List of strings representing topics.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
