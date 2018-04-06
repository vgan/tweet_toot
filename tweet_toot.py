#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, sys
from keys import *
from random import choice
from mastodon import Mastodon

mastodon = Mastodon(
        api_base_url='https://mastodon.social',
        client_id = '/home/vgan/twoot/twoot_clientcred.txt',
        access_token = '/home/vgan/twoot/twoot_usercred.txt'
)
auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_token_key, twitter_token_secret)
api = tweepy.API(auth)

text = sys.argv[1]
length = len(text)

if length <= 279:
        print str(length) + " characters..."
        if length == 69:
                print "nice."
        try:
                status = api.update_status(status=text)
                print "tweeted."
        except:
                print "twete failed :("
        try:
                tooterino = mastodon.status_post(text, sensitive=False)
                print "tooted."
        except:
                print "awoo failed :(("
else:
        thismany = length - 280
        print str(length) + " is " + str(thismany) + " too many characters for twitter."
