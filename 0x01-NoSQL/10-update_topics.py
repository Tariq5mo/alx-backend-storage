#!/usr/bin/env python3
"""
Module for updating topics in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on the name

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object
        name (str): The school name to update
        topics (list of str): The list of topics approached in the school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
