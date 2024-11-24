#!/usr/bin/env python3
"""
Module for updating topics in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on the name

    Args:
        mongo_collection (_type_): _description_
        name (_type_): _description_
        topics (_type_): _description_
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
