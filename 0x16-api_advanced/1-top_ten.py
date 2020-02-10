#!/usr/bin/python3
""" Queries Reddit API for first 10 hot post titles from subreddit
    Prints 'None' if invalid subreddit
"""
import requests as r
import requests.auth as ra
from sys import argv


def top_ten(subreddit):

    # Generates token & bearer for requests to oauth.reddit.com endpoints
    # https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example

    client_id = "i_m3aNLQE0vskA"
    secret = "UykV3Qz2TGSWSWaMmSeOWgR5JT4"
    my_username = "causticpop"
    my_pwd = "Holberton98"

    client_auth = ra.HTTPBasicAuth(client_id, secret)
    post_data = {"grant_type": "password", "username":
                 my_username, "password": my_pwd}
    headers = {"User-Agent": "ChangeMeClient/0.1 by {}".format(my_username)}
    response = r.post("https://www.reddit.com/api/v1/access_token",
                      auth=client_auth, data=post_data, headers=headers)
    token = response.json().get("access_token")
    bearer = response.json().get("token_type")

    # Queries oauth.reddit.com endpoints using token & bearer
    # Sets limit on number of items returned in params variable

    subreddit = argv[1]
    sub_url = "https://oauth.reddit.com/r/{}/hot".format(subreddit)

    headers = {"Authorization": "{} {}".format(bearer, token),
               "User-Agent": "ChangeMeClient/0.1 by {}".format(my_username)}
    params = {'limit': 10}
    response = r.get(sub_url, headers=headers, params=params)

    # handles error response; invalid subreddit
    if response.status_code is not 200:
        print("None")
    # peels the onion of nested dicts and lists
    else:
        response_json = response.json().get('data').get('children')
        for subdict in response_json:
            print(subdict.get('data').get('title'))
