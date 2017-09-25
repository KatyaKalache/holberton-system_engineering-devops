#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    if subreddit is None:
        return 0
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    req = requests.get(subreddit, headers=headers)
    if req.status_code == 301:
        return 0
    subscribers = req.json().get('data', {}).get('subscribers')
    if subscribers is None:
        return 0
    return subscribers
