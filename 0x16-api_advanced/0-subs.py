#!/usr/bin/python3
"""module:
    number_of_subscribers:
        is a function that queries the Reddit API and returns
            the number of subscribers
    """
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = requests.get(URL, allow_redirects=False)
    if data.status_code == 200:
        json_format = data.json()
        return json_format['data']['subscribers']
    return 0
