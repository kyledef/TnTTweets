import tweepy
from tweepy import Stream
from common import *
from tweepy.streaming import StreamListener

def process_tweet_filter(tweet):
	# print tweet
	print tweet.text
	print tweet.user.name

	if tweet.entities:
		print tweet.entities
	else:
		print "No entities"

class MyYoutubeListener(StreamListener):
	def on_error(self, status_code):
		process_errors(repr(status_code))
		return True

	def on_event(self, status):
		print "received event"
		process_tweet_filter(status)
		return True

	def on_direct_message(self, status):
		print "received direct message"
		process_tweet_filter(status)
		return True

	def on_status(self, status):
		print "received status"
		process_tweet_filter(status)
		return True

#peusdo main function
def runner():
	auth = getAuthentication()
	if auth:
		print "Authentication"
		m_listener = MyYoutubeListener()
		m_streamer = Stream(auth,m_listener)
		m_streamer.filter(track=['#YouTubeAsksObama'])
	else:
		print "Problem with the Authentication"

runner()