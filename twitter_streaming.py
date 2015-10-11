
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3929767222-GMfEim78KAQMqb4BP7gMva46kXXBrFt5HFr0kca"
access_token_secret = "UPnD92ncl5XSFvGrP8WKc5qOKdcPFtCQvrUhmGBOj91m3"
consumer_key = "Jh47JH54FQnQkCsDv7Kr2aq7d"
consumer_secret = "amXdnvILRcvrGM9iOhfVgQ8FnFSEkwrlNCXDXYaqS5tgHnRcwC"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['twibblets'])