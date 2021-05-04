#!/usr/bin/python3
"""
Export data in the JSON format.
"""

from sys import argv
import json
import requests


if __name__ == "__main__":

    evt = 'https://jsonplaceholder.typicode.com/users/'
    username = requests.get(evt + argv[1])
    username = username.json()['username']

    todos = requests.get(evt + argv[1] + '/todos/')
    tasks = []
    for items in todos.json():
        tasks.append({"task": items['title'],
                     "completed": items['completed'], "username": username})

    with open(argv[1] + ".json", 'w') as data:
        json.dump({argv[1]: tasks}, data)
