#!/usr/bin/env python3
"""
A Python script that provides some statistics about Nginx logs stored
in MongoDB.

Database: logs
Collection: nginx

The script displays:
- The total number of logs in the collection.
- The number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
- The number of logs where the method is GET and the path is /status.

Usage:
1. Ensure MongoDB is running and accessible at mongodb://127.0.0.1:27017.
2. Restore the provided dump file using mongorestore.
3. Run this script to display the statistics.

Example output:
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    get = nginx_collection.count_documents({"method": "GET"})
    post = nginx_collection.count_documents({"method": "POST"})
    put = nginx_collection.count_documents({"method": "PUT"})
    patch = nginx_collection.count_documents({"method": "PATCH"})
    delete = nginx_collection.count_documents({"method": "DELETE"})
    status = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{nginx_collection.count_documents({})} logs' +
          '\n' + 'Methods:' +
          '\n' +
          f'\tmethod GET: {get}' +
          '\n' +
          f'\tmethod POST:{post}' +
          '\n' +
          f'\tmethod PUT:{put}' +
          '\n' +
          f'\tmethod PATCH:{patch}' +
          '\n' +
          f'\tmethod DELETE:{delete}' +
          '\n' +
          f'{status} status check')
