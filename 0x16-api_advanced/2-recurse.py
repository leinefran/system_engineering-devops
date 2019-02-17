#!/usr/bin/python3
'''A recursive function that queries the Reddit API and returns the titles of
the hot posts for a given subreddit'''
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):

    try:
        req = requests.get('https://api.reddit.com/r/{}/hot?after={}'
                           .format(subreddit, after),
                           allow_redirects=False,
                           headers={'User-Agent': 'Frankie'})

        print("The value of subRe_info is {}".format(req))
        print("")

        subRe_info = req.json()
        print("The value of subRe_info is {}". format(subRe_info))
        print("")

        top_ten = subRe_info.get('data').get('children')
        for k in top_ten:
            hot_list.append(k.get('data').get('title'))

        after = subRe_info.get('data').get('after')
    except:
        return(None)

    if (after is None):
        return(hot_list)
    else:
        return(recurse(subreddit, hot_list, after))
