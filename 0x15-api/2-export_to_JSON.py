#!/usr/bin/python3
"""import module
"""
import json
import re
import requests
import sys


def GET(id):
    """GET : is function that get requests and print with right format"""
    URL = f'https://jsonplaceholder.typicode.com'
    USERS = requests.get(f"{URL}/users/{id}").json()
    TODOS = requests.get(f"{URL}/todos").json()
    users_data = {}
    for user in USERS:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, TODOS))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)


if __name__ == "__main__":
    if len(sys.argv) > 1 and re.fullmatch(r'\d+', sys.argv[1]):
        id = int(sys.argv[1])
        GET(id)
