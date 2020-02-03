#!/usr/bin/python3
""" Queries REST API for employee info
    argv 1 = int employee ID
"""
if __name__ == "__main__":
    import requests as r
    from sys import argv

    # Finds employee name by "id" param in /users/
    name_q = r.get("https://jsonplaceholder.typicode.com/users/{}/"
                   .format(argv[1]))
    data = name_q.json()
    employee_name = data.get("name")

    # Finds employee tasks by "userID" param; /users/ & /todo/ are linked
    url = "https://jsonplaceholder.typicode.com/users/1/todos/"
    task_q = r.get(url, params={'userId': argv[1]})
    data = task_q.json()

    # Finds total number of tasks
    task_total = len(data)

    # Finds total number of completed tasks
    task_completed = 0
    for dicts in data:
        for k, v in dicts.items():
            if k == 'completed' and v is True:
                    task_completed += 1

    # Prints first line in specified format:

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, task_completed, task_total))

    # Prints subsequent lines as titles of completed tasks:

    for dicts in data:
        for k, v in dicts.items():
            if k == 'completed' and v is True:
                    print("\t {}".format(dicts['title']))
