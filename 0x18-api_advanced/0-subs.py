#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None:
        return 0
    headers = {'user-agent': 'info'}
    subreddit = 'https://www.reddit.com/r/subreddit/about.json'
    req = requests.get(subreddit, headers=headers).json()
    if (req.get('error')):
        return 0
    data = req.get('data')
    subscribers = data.get('subscribers')
    return subscribers
