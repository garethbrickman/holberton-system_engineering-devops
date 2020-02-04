#!/usr/bin/python3
""" Queries REST API for employee info, exports to JSON
    argv 1 = int employee ID
"""
if __name__ == "__main__":
    import json
    import requests as r
    from sys import argv

    user_id = argv[1]
    # Finds employee username by "id" param in /users/
    name_q = r.get("https://jsonplaceholder.typicode.com/users/{}/"
                   .format(user_id))
    data = name_q.json()
    username = data.get("username")

    # Finds employee tasks by "userID" param; /users/ & /todo/ are linked
    url = "https://jsonplaceholder.typicode.com/users/1/todos/"
    task_q = r.get(url, params={'userId': user_id})
    data = task_q.json()

    # Creates JSON object with request data, writes to .json file

    json_dict = {}
    json_list = []

    for elem in data:
        json_dict["task"] = elem.get("title")
        json_dict["completed"] = elem.get("completed")
        json_dict["username"] = username
        json_list.append(json_dict)
        json_dict = {}

    json_data = {}
    json_data[user_id] = json_list
    with open(user_id + ".json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)
