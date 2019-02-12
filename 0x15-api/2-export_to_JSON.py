#!/usr/bin/python3
'''A Python script that, using REST API, for a given employee ID,
returns information about their TODO list progress'''

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    req_user = requests.get('https://jsonplaceholder.typicode.com/users')
    users = req_user.json()
    for user in users:
        if int(user_id) == user.get('id'):
            user_name = user.get('name')
            username = user.get('username')

    req_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = req_tasks.json()
    json_filename = sys.argv[1] + ".json"
    data = {}
    list_value = []
    with open(json_filename, 'w') as jsonfile:
        for task in todo_list:
            if int(user_id) == task.get('userId'):
                list_value.append({"task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": username})
        data[user_id] = list_value
        json.dump(data, jsonfile)
