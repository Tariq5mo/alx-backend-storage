#!/usr/bin/env python3
"""
Module for inserting a new document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        The new _id of the inserted document.
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
