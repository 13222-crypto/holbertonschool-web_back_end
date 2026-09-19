#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Contains function to find schools that cover a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    :param mongo_collection: pymongo collection object
    :param topic: (string) topic searched
    :return: list of matching school documents
    """
    return list(mongo_collection.find({"topics": topic}))
