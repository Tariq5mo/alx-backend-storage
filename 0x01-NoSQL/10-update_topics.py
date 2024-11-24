"""
	"""


def update_topics(mongo_collection, name, topics):
    """Update all topics of a school document based on the name

    Args:
        mongo_collection (_type_): _description_
        name (_type_): _description_
        topics (_type_): _description_
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
