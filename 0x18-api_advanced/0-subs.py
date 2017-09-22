#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    if subreddit is None:
        return 0
    req = requests.get(subreddit, headers=headers).json()
    data = req.get('data')
    subscribers = data.get('subscribers')
    if subscribers is None:
        return 0
    return subscribers
