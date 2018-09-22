#authentication code here
from  flask import Flask ,jsonify,Response

import tweepy
from tweepy import OAuthHandler
from urllib.parse import urlencode
import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from tweepy.api import API

app=Flask(__name__)

consumer_key='zxwYSCOEug42LjRggdEsRJXo2'
consumer_secret='KBgqcB0BDqH8ORacjaFqzM2N5qFgBskUx1wBm0FIaXlHf1RT5V'
access_key='714494503822856193-fr3FGqtnNF0DnBHG4l6x56MRCdFmPwQ'
access_secret='WReLl0jPAEHNCBZ3y2Ip8a1lyAWCZZuwbwjfZ70XOUo6G'

auth = OAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_key,access_secret)
