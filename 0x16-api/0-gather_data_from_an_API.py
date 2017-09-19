#!/usr/bin/python3
"""Returns information about an employee TODO list progress"""
import requests
from sys import argv

if __name__ == "__main__":
    req_todos = 'https://jsonplaceholder.typicode.com/todos'
    req_users = 'https://jsonplaceholder.typicode.com/users'
    EMPLOYEE_ID = argv[1]
    EMPLOYEE_NAME = requests.get(req_users + "/" +
                                 str(EMPLOYEE_ID)).json().get("name")
    task_complete = 0
    task_incomplete = 0

    full_dict = requests.get(req_todos).json()
    result = []

    for i in full_dict:
        if int(EMPLOYEE_ID) is (i.get('userId')):
            if i.get("completed"):
                result.append(i.get("title"))
                task_complete += 1
            if i.get("completed") is False:
                task_incomplete += 1

    tasks_total = task_complete + task_incomplete

    print ("Employee", EMPLOYEE_NAME, "is done with tasks({:d}/{:d}):".
           format(task_complete, tasks_total))

    for each in result:
        print ("\t", each)
