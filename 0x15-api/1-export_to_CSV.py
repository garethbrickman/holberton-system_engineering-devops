#!/usr/bin/python3
""" Queries REST API for employee info, exports to CSV
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    argv 1 = int employee ID
"""
if __name__ == "__main__":
    import csv
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

    # Creates csv file, writes request data into it row by row

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        csv_data = csv.writer(csvfile, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for elem in data:
            csv_data.writerow([elem["userId"], username,
                               elem["completed"], elem["title"]])
