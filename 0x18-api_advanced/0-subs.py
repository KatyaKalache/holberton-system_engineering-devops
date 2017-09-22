#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    subreddit = 'https://www.reddit.com/r/subreddit/about.json'
    req = requests.get(subreddit).json()
    data = req.get('data')
    subscribers = data.get('subscribers')
    return subscribers
