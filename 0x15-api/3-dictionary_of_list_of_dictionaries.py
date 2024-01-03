#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    All_to_be_done = {}

    for user in users:
        All_tasks = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                model_dict = {
                        "username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
                All_tasks.append(model_dict)
        All_to_be_done[user.get('id')] = All_tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(All_to_be_done, f)
