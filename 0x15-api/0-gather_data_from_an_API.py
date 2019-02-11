#!/usr/bin/python3
'''A Python script that, using REST API, for a given employee ID, returns information about their TODO list progress'''

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    req_user = requests.get('https://jsonplaceholder.typicode.com/users')
    users = req_user.json()
    for user in users:
        if int(user_id) == user.get('id'):
            user_name = user.get('name')

    req_tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = req_tasks.json()
    count_tasks = 0
    done_tasks = 0
    for task in todo_list:
        if int(user_id) == task.get('userId'):
            count_tasks = count_tasks + 1
            if task.get('completed') == True:
                done_tasks = done_tasks + 1

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                    done_tasks, count_tasks))


    for task in todo_list:
        if int(user_id) == task.get('userId'):
            if task.get('completed') == True:
                task_title = task.get('title')
                print("\t {}".format(task_title))
