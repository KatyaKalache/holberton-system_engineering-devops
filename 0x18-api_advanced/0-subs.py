#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit = 'https://www.reddit.com/r/subreddit/about.json'
    req = requests.get(subreddit, headers).json()
    if (req.get('error')):
        return 0
    data = req.get('data')
    subscribers = data.get('subscribers')
    return subscribers
