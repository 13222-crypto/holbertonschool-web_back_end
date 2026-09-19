#!/usr/bin/env python3
"""
Module 101-students
Contains function top_students to return all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    :param mongo_collection: pymongo collection object
    :return: list of student documents with averageScore key, sorted descending
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "topics": "$topics",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
