import pandas as pd
import tweepy
import config

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

keywords = 'covid'
limit = 10000
ph = '14.589119422692292,121.0263763730469,17097.55km'


tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang = 'en', geocode = ph, count = 200, tweet_mode = 'extended').items(limit)

colums = ['Time', 'User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=colums)

#print(df)

df.to_csv('dataset7_tweets.csv')