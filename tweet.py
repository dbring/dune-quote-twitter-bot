import requests
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# API request for Dune quote
response = requests.get('https://the-dune-api.herokuapp.com/quotes').json()

# Dune quote
quote = response[0]['quote']

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Post tweet
api.update_status(quote)
