#!/usr/bin/python3
'''A function that queries the Reddit API and returns the number of subscribers
for a given subreddit'''
import requests
import sys


def number_of_subscribers(subreddit):

    try:
        req_subreddit = requests.get('https://api.reddit.com/r/{}/about'.
                                     format(subreddit), allow_redirects=False,
                                     headers={'User-Agent': 'Frankie'})

        subr_info = req_subreddit.json()

        subscribers = subr_info.get('data').get('subscribers')
        return subscribers

    except:
        return 0
