#!/usr/bin/python3
"""import module"""
import requests
from sys import argv
import re


def GET(id):
    """GET : is function that get requests and print with right format"""
    URL = f'https://jsonplaceholder.typicode.com'
    USERS = requests.get(f"{URL}/users/{id}").json()
    TODOS = requests.get(f"{URL}/todos").json()
    # print(USERS)
    # print(TODOS)
    EMPLOYEE_NAME = USERS.get('name')
    TOTAL_NUMBER_OF_TASKS = list(filter(
        lambda x: x.get('userId') == id,
        TODOS
    ))
    NUMBER_OF_DONE_TASKS = list(filter(
        lambda x: x.get('completed'),
        TOTAL_NUMBER_OF_TASKS
        ))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, len(NUMBER_OF_DONE_TASKS),
        len(TOTAL_NUMBER_OF_TASKS)
    ))
    for TODO_DONE in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(
            TODO_DONE.get('title')
        ))


if __name__ == "__main__":
    if len(argv) > 1 and re.fullmatch(r'\d+', argv[1]):
        id = int(argv[1])
        GET(id)
