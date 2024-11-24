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


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx
print(f'{nginx_collection.count_documents({})} logs' +
      '\n' + 'Methods:' +
      '\n' +
      f'\tmethod GET: {nginx_collection.count_documents({"method": "GET"})}' +
      '\n' +
      f'\tmethod POST:
      {nginx_collection.count_documents({"method": "POST"})}' +
      '\n' +
      f'\tmethod PUT:
      {nginx_collection.count_documents({"method": "PUT"})}' +
      '\n' +
      f'\tmethod PATCH:
      {nginx_collection.count_documents({"method": "PATCH"})}' +
      '\n' +
      f'\tmethod DELETE:
      {nginx_collection.count_documents({"method": "DELETE"})}' +
      '\n' +
      f'{nginx_collection.count_documents(
          {"method": "GET", "path": "/status"})} status check')


if __name__ == "__main__":
    pass
