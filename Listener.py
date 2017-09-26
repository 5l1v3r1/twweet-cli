import tweepy
import os
import csv
import json
import sys
from os.path import expanduser
from config.ConfigReader import ConfigurationReader
from importlib import reload

# Twitter API credentials
cfg = {}
home = expanduser("~")
Configuration = ConfigurationReader()
TweetsStorage = Configuration.GetTweetsStorage()
HashTagStorage = Configuration.GetTweetsStorage()

'''STREAM'''

class StreamListener(tweepy.StreamListener):
    # Decided I would keep all the overridable functions from the BaseClass so we know what we have to play with.
    def __init__(self, time_limit=60):
        super(StreamListener, self).__init__(api)

    def on_status(self, status):
        print('@{} => {}'.format(status.user.screen_name, status.text.replace("\n", " ")))

    def on_error(self, status_code):
        print('AN ERROR: {}'.format(status_code))
    #   read the docs and handle different errors

    def keep_alive(self):
        """Called when a keep-alive arrived"""
        return

    def on_exception(self, exception):
        """Called when an unhandled exception occurs."""
        return

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        return

    def on_event(self, status):
        """Called when a new event arrives"""
        return

    def on_direct_message(self, status):
        """Called when a new direct message arrives"""
        return

    def on_friends(self, friends):
        """Called when a friends list arrives.

        friends is a list that contains user_id
        """
        return

    def on_limit(self, track):
        """Called when a limitation notice arrives"""
        return

    def on_timeout(self):
        """Called when stream connection times out"""
        return

    def on_disconnect(self, notice):
        """Called when twitter sends a disconnect notice

        Disconnect codes are listed here:
        https://dev.twitter.com/docs/streaming-apis/messages#Disconnect_messages_disconnect
        """
        return

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        return

class Listener():
    
    def __init__(self, twweeterObj):
        self.twweeterObj = twweeterObj
        self.streamListenerOB = StreamListener()

    # authorise the stream listener
    def authStreamer(self):
        stream = tweepy.Stream(auth=self.twweeterObj.api.auth, listener=self.streamListenerOB)
        return stream

    #Listen for tweets on the current users timeline
    def streamYourTL(self):
        stream = self.authStreamer()
        stream.userstream(_with='following', async=True)

    #listen for tweets containing a specific word or hashtag (a phrase might work too)
    def streamWordOrHashtag(self, wordsList):
        stream = self.authStreamer()
        stream.filter(track=wordsList, async=True)

'''END STREAM'''





