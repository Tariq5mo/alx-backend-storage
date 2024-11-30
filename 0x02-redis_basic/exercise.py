#!/usr/bin/env python3
"""
This module defines a Cache class to interact with a Redis database.
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Cache class to interact with Redis.
    """

    def __init__(self):
        """
        Initialize the Cache class.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a randomly generated key.

        Args:
            data (str | bytes | int | float): The data to store in Redis.

        Returns:
            str: The randomly generated key used to store the data.
        """
        random_key = uuid4()
        self._redis.set(str(random_key), data)
        return str(random_key)
