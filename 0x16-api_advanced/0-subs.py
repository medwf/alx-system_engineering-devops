#!/usr/bin/python3
"""number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    headers = {'User-Agent': 'Chrome'}
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = requests.get(URL, allow_redirects=False, headers=headers)
    if data.status_code == 200:
        json_format = data.json()
        return json_format["data"]["subscribers"]
    return 0
