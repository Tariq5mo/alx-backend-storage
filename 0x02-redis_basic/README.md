# 0x02. Redis Basic

## Description

This project focuses on the basics of using Redis, a powerful in-memory data structure store, as a backend for various applications. The tasks cover basic operations, caching, and tracking with Redis.

## Learning Objectives

- Learn how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- Your code should use the `pycodestyle` style (version 2.5).
- All modules should have documentation.
- All classes should have documentation.
- All functions and methods should have documentation.
- All functions and coroutines must be type-annotated.

## Installation

To install Redis on Ubuntu 18.04:

```sh
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

To use Redis in a container:

```sh
service redis-server start
```

## Tasks

### 0. Writing strings to Redis

Create a `Cache` class with methods to store data in Redis and return the key.

### 1. Reading from Redis and recovering original type

Create a `get` method to retrieve data from Redis and convert it back to the original format.

### 2. Incrementing values

Implement a system to count how many times methods of the `Cache` class are called using a decorator.

### 3. Storing lists

Define a `call_history` decorator to store the history of inputs and outputs for a particular function.

### 4. Retrieving lists

Implement a `replay` function to display the history of calls of a particular function.

### 5. Implementing an expiring web cache and tracker (Advanced)

Implement a `get_page` function to cache the HTML content of a URL with an expiration time of 10 seconds.

## Author

Tariq Omer, a student in ALX SE (Back-end)
