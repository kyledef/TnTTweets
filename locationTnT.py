import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from common import *

globalFile = None
globalIgnoreFile = None



# develop a process tweet to make dealing with acquired tweets consistent
def process_tweet_loc(tweet, location=False):
	global globalFile
	
	if location:
		if tweet.geo:
			print tweet.geo
		else:
			print "no location found"

		if tweet.place:
			print tweet.place.name
			print tweet.place.country_code
			print tweet.place.country
		else:
			print "no place info found"

	if globalFile:
		if isinstance(tweet, six.string_types):
			globalFile.write(tweet)
		else:
			globalFile.write(getattr(tweet, "_json"))
	# else:
	# 	print tweet

def process_ignored(raw_data):
	global globalIgnoreFile
	if globalIgnoreFile == None:
		globalIgnoreFile = open("ignored.json", "a")
	globalIgnoreFile.write(raw_data)

#After Creating the basic Listener we can develop more complex functionality with the listener
class MyLocationListener(StreamListener):
	def on_error(self, status_code):
		process_errors(repr(status_code))
		return True

	def on_event(self, status):
		print "received event"
		process_tweet_loc(status, True)
		return True


	def on_direct_message(self, status):
		print "received direct message"
		process_tweet_loc(status, True)
		return True
		

	def on_status(self, status):
		print "received status"
		process_tweet_loc(status, True)
		return True
		

#peusdo main function
def runner():
	trinbago_loc="-86.000 10.000 -60.500 21.000"
	global globalFile
	loc = []
	for l in trinbago_loc.split():
		loc.append(float(l))

	auth = getAuthentication()
	# globalFile = open("result.json", "a")
	if auth:	
		# api = tweepy.API(auth)
		# m_listener =  MyListener()
		m_listener =  MyLocationListener()
		m_streamer = Stream(auth,m_listener)
		m_streamer.filter(locations=loc)
		# m_streamer.sample() #Will access the twitter public streaming api via the sample method

#Run program
runner()