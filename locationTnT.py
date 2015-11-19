import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from common import *
import six
import json

globalFile = None
globalIgnoreFile = None

# develop a process tweet to make dealing with acquired tweets consistent
def process_tweet_loc(tweet, location=False):
	global globalFile
	if tweet.place:
		if tweet.place.country_code == "TT":
			# print "Place: "+tweet.place.name+" Code: " + tweet.place.country_code + " Country: " + tweet.place.country
			print "Text: " + tweet.text
			print tweet.user.screen_name + " has " + str(tweet.user.followers_count) + " friends"
			globalFile.write(json.dumps(getattr(tweet, "_json")) + "\n")

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
		# print "received status"
		process_tweet_loc(status, True)
		return True
		

#peusdo main function
def runner():
	trinbago_loc="-61.560 10.200 -60.300 11.120"
	global globalFile
	loc = []
	for l in trinbago_loc.split():
		loc.append(float(l))

	auth = getAuthentication()
	globalFile = open("result.json", "a")
	if auth:	
		# api = tweepy.API(auth)
		# m_listener =  MyListener()
		m_listener =  MyLocationListener()
		while True:
			try:
				m_streamer = Stream(auth,m_listener)
				m_streamer.filter(locations=loc)
			except:
				continue

		# m_streamer.sample() #Will access the twitter public streaming api via the sample method

if __name__ == "__main__":
	#Run program
	runner()