#!/usr/bin/env python3
"""
Module for retrieving schools by topic in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object
        topic (str): The topic to search for

    Returns:
        list: List of schools having the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass
