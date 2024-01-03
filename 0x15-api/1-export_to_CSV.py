#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import csv
    import requests
    import sys

    userId = sys.argv[1]
    d = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(userId))
    a = d.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, a, str(task.get('completed')),
                                 task.get('title')])
