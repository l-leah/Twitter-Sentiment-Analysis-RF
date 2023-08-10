import snscrape.modules.twitter as sntwitter
import pandas as pd

query ="@inquirerdotnet lockdown lang:en"
tweets = []
limit = 10000

for tweet in sntwitter.TwitterHashtagScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

#print(df)

df.to_csv("inquirer7 tweets.csv")