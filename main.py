import logging
from time import sleep
import time
import os
from os import environ
import logging
import  tweepy
from tweepy import OAuthHandler
from tweepy import API


logging.basicConfig()
logger = logging.getLogger("BOT")
logger.setLevel(logging.DEBUG)

INTERVAL = 5 * 60 * 1  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
key = environ['ACCESS_KEY']
secret = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

INTERVAL = 5 * 60 * 1  # tweet every 6 hours

while True:
    print("about to get ad...")
    api.update_status("hello Test")
    time.sleep(INTERVAL)
    
