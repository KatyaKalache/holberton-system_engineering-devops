#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def top_ten(subreddit):
    """Returns top ten posts"""
    title_list = []
    counter = 0
    if subreddit is None:
        print ("None")
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(subreddit, headers=headers)
    if (req.status_code == 301):
        print ("None")
    top_ten = req.json().get('data', {}).get('children')[:10]
    if top_ten is None:
        print ("None")
    for each in top_ten:
        title_list.append(each.get('data').get('title'))
        if (counter != 9):
            title_list.append('\n')
        string_format = ''.join(title_list)
        counter += 1
    print (string_format)
