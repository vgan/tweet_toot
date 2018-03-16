#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
from keys import *
from mastodon import Mastodon
import sys

mastodon = Mastodon(
        api_base_url='https://mastodon.social',
        client_id = '/home/vgan/tweet_toot/tweet_toot_clientcred.txt',
        access_token = '/home/vgan/tweet_toot/tweet_toot_usercred.txt'
)
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_token_key, twitter_token_secret)
api = tweepy.API(auth)

text = sys.argv[1]

try:
        status = api.update_status(status=text)
except:
        print "tweet failed"

try:
        tooterino = mastodon.status_post(text, sensitive=False)
except:
        print "toot failed"
