#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID
"""


import requests
from sys import argv

if __name__ == "__main__":
    evt = 'https://jsonplaceholder.typicode.com/todos/'
    user = requests.get(evt + argv[1])
    employee = user.json()['name']

    todos = requests.get(evt + argv[1] + '/todos')
    total = todos.json()
    ready = []
    for dic in total:
        if dic['completed']:
            ready.append(dic['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(employee, len(ready), len(total)))
    #for task in ready:
        #print('\t', task)
