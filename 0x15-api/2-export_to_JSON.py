#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    a = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    toda_a = {}
    all_tasks = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": a.json().get('username')}
            all_tasks.append(taskDict)
    toda_a[userId] = all_tasks

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(toda_a, f)
