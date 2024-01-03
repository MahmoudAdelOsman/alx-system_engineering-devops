#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    xx = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            xx += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, xx))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
