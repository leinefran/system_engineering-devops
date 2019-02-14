#!/usr/bin/python3
'''A recursive function that queries the Reddit API and returns the titles of
the hot posts for a given subreddit'''
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):

    try:
        if (after):
            req = requests.get('https://api.reddit.com/r/{}/hot'
                               .format(subreddit), allow_redirects=False,
                               headers={'User-Agent': 'Frankie'})
        else:
            (requests.get('https://api.reddit.com/r/{}/hot?after={}'
                           .format(subreddit, id_after), allow_redirects=False,
                           headers={'User-Agent': 'Frankie'})):

        subRe_info = req.json()

        top_ten = subRe_info.get('data').get('children')
        for k in top_ten:
            hot_list.append(k.get('data').get('title'))

        id_after = subRe_info.get('data').get('after')

        if (after):
            return(recurse(subreddit, hot_list, after))
        else:
            return(hot_list)

    except:
        return(None)
