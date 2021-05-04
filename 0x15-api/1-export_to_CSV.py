#!/usr/bin/python3
"""Using what you did in the task #0,
    extend your Python script to export data in the CSV format.
"""

from sys import argv
import csv
import requests


if __name__ == "__main__":

    evt = 'https://jsonplaceholder.typicode.com/users/'
    username = requests.get(evt + argv[1])
    user = username.json()['username']
    tasks = []
    todos = requests.get(evt + argv[1] + "/todos/")
    for items in todos.json():
        tasks.append([items["userId"], user,
                           items['completed'], items['title']])

    with open(str(tasks[0][0]) + '.csv', 'w') as file:
        write = csv.writer(file, quoting=csv.QUOTE_ALL)
        write.writerows(tasks)
