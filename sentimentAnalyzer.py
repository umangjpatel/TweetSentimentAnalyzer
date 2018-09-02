#Import the tweepy package for accessing Twitter APIs in Python
import tweepy
#Import textblob package for sentiment anaysis of each tweet fetched from the API
from textblob import TextBlob
#Import the csv package for storing the tweets in csv file
import csv

#API Keys required for supporting the usage of the Twitter APIs
#Access and Consumer keys and secret for authenticating this script to work with the Twitter API
consumer_key = "Your Consumer Key>"
consumer_secret = "Your Consumer Secret Key>"
access_token = "Your Access Token Key>"
access_token_secret = "<Your Access Token Secret Key>"

#Authenticating with Twitter for using its API provided he above keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#API variable for communicating our actions to the Twitter APIs
api = tweepy.API(auth)

#Asking the topic from the tweet_use
tweet_search_topic = input("What topic you want to find ? : ")

#Storing the tweets
public_tweets = api.search(tweet_search_topic)

#Opening the dataset.csv filefor writinh the tweets in it
with open('dataset.csv', mode='w') as tweets_file:
    tweet_writer = csv.writer(tweets_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    #Labelling the columns for the tweet dataset
    tweet_writer.writerow(['Tweet', 'Author', 'Date', 'Sentiment Polarity'])
    #Analyzing each tweet from the tweets list and storing it in a csv file
    for tweet in public_tweets:
        tweet_text = tweet.text
        tweet_user = tweet.user.name
        tweet_created_at = tweet.created_at
        tweet_sentiment = TextBlob(tweet_text).sentiment.polarity
        print(tweet_text, tweet_user, tweet_created_at)
        print("Sentiment is %f" % tweet_sentiment)
        tweet_writer.writerow([tweet_text, tweet_user, tweet_created_at, tweet_sentiment])
