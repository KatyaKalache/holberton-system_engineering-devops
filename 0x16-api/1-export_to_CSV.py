#!/usr/bin/python3
"""Returns information about an employee TODO list progress"""
import requests
from sys import argv
import csv

if __name__ == "__main__":
    req_todos = 'https://jsonplaceholder.typicode.com/todos'
    req_users = 'https://jsonplaceholder.typicode.com/users'
    EMPLOYEE_ID = argv[1]
    EMPLOYEE_NAME = requests.get(req_users + "/" +
                                 str(EMPLOYEE_ID)).json().get("name")

    full_dict = requests.get(req_todos).json()
    result = []

    for i in full_dict:
        if int(EMPLOYEE_ID) is (i.get('userId')):
            result.append([EMPLOYEE_ID, EMPLOYEE_NAME, i.get("completed"),
                           i.get("title")])

    csv_file = "{}.csv".format(EMPLOYEE_ID)

    with open(csv_file, 'wt') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for value in result:
            writer.writerow(value)
