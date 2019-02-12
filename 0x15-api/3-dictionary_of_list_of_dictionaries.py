#!/usr/bin/python3
'''A Python script that, using REST API, for a given employee ID,
returns information about their TODO list progress'''

import json
import requests
import sys

if __name__ == "__main__":
    req_user = requests.get('https://jsonplaceholder.typicode.com/users')
    users = req_user.json()

    req_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = req_tasks.json()

    json_filename = "todo_all_employees.json"
    data = {}

    with open(json_filename, 'w') as jsonfile:
        for user in users:
            username = user.get('username')
            user_id = user.get('id')
            list_value = []
            for task in todo_list:
                if user_id is task.get('userId'):
                    list_value.append({"task": task.get('title'),
                                       "completed": task.get('completed'),
                                       "username": username})
            data[user_id] = list_value
        json.dump(data, jsonfile)
