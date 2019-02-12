#!/usr/bin/python3
'''A Python script that, using REST API, for a given employee ID,
returns information about their TODO list progress'''

import csv
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
    csv_filename = sys.argv[1] + ".csv"
    with open(csv_filename, 'w') as csvfile:
        for task in todo_list:
            if int(user_id) == task.get('userId'):
                data = [user_id, username, task.get('completed'),
                        task.get('title')]
                task_record = csv.writer(csvfile, delimiter=",",
                                         quoting=csv.QUOTE_ALL)
                task_record.writerow(data)
