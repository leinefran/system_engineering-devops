#!/usr/bin/python3
'''A function that queries the Reddit API and prints the titles of the 1st 10
hot posts for a given subreddit'''
import requests
import sys


def top_ten(subreddit):

    try:
        req_subreddit = requests.get('https://api.reddit.com/r/{}/hot?sort=hot&
        limit=10'.format(subreddit), allow_redirects=False,
                                     headers={'User-Agent': 'Frankie'})

        subRe_info = req_subreddit.json()

        ten_hot_posts = subRe_info.get('data').get('children')
        return ten_hot_posts

    except:
        return 0
