#!/usr/bin/env python3
"""
This module defines a Cache class to interact with a Redis database.
"""
import redis
from typing import Union, Callable, Optional
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

    # Task 2

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None,
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve from Redis.
            fn (Optional[Callable[[bytes], Union[str, bytes, int, float]]],
                                                                    optional):
                A function to convert the data back to the desired format.
                                                            Defaults to None.

        Returns:
            Union[str, bytes, int, float]: The retrieved data,
                                        optionally converted by fn.
        """
        result = self._redis.get(key)
        if result is None:
            return None
        if fn:
            return fn(result)
        else:
            return result

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            str: The retrieved string.
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            int: The retrieved integer.
        """
        return self.get(key, int)
