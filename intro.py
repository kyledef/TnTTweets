import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener


from credentials import *

def getAuthenticatoin():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except:
		return None



def displayHomeTweets(api):
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
	    print tweet.text

def displayFriends(api):
	for friend in tweepy.Cursor(api.friends).items():
		print friend


#Create a class to handle events within the stream: https://github.com/tweepy/tweepy/blob/master/examples/streaming.py
class MyListener(StreamListener): #Extending the StreamListener
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status



def runner():
	auth = getAuthenticatoin()
	if auth:	
		api = tweepy.API(auth)
		# displayFriends(api)
		# displayHomeTweets(api)

		m_listener = MyListener()
		m_stream = Stream(auth, m_listener)

		m_stream.sample()

runner()