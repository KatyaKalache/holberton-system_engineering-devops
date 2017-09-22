#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(subreddit, headers=headers).json()
    if (req.get('error')):
        return 0
    data = req.get('data')
    top_ten = data.get('children')

    for each in top_ten:
        return (each)
