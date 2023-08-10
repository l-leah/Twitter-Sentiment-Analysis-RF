import tweepy
from tweepy import OAuthHandler
import joblib
from flask import Flask, request, render_template

from flask import Flask, render_template, request

# Load the pretrained model
model = joblib.load('RF_model.pkl')


def get_tweet_sentiment(tweet):
    twitter_data = [str(x) for x in tweet]
    predictions = model.predict(twitter_data)[0]
    if predictions == 0:
        return 'Negative'
    else:
        return 'Positive'


def get_tweets(api, count):
    count = int(count)
    query = 'covid'
    tweets = []
    try:
        fetched_tweets = tweepy.Cursor(api.search_tweets, q=query, lang='en',
                                       geocode='14.589119422692292,121.0263763730469,17097.55km', tweet_mode='extended').items(count)
        for tweet in fetched_tweets:
            parsed_tweet = {}
            if 'retweeted_status' in dir(tweet):
                parsed_tweet['text'] = tweet.retweeted_status.full_text
            else:
                parsed_tweet['text'] = tweet.full_text
            parsed_tweet['sentiment'] = get_tweet_sentiment(
                parsed_tweet['text'])
            if tweet.retweet_count == 0:
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
        return tweets
    except tweepy.TweepyException as e:
        print("Error : " + str(e))


app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def home():
    return render_template("index.html")

# ******Phrase level sentiment analysis


@app.route("/predict", methods=['POST', 'GET'])
def pred():
    if request.method == 'POST':
        count = request.form['num']
        fetched_tweets = get_tweets(api, count)
        return render_template('result.html', result=fetched_tweets)


@app.route("/predict1", methods=['POST', 'GET'])
def pred1():
    new_tweet = [str(x) for x in request.form.values()]
    predictions = model.predict(new_tweet)[0]
    if predictions == 0:
        return render_template('result1.html', msg=new_tweet, result='Negative')
    else:
        return render_template('result1.html', msg=new_tweet, result='Positive')


if __name__ == '__main__':

    consumer_key = 'v8DDc153EKW6HOkwztY1wHDRg'
    consumer_secret = '8VIFmdCJ5DNe0ma25RgYauQRFXRXz5dqGjjHpsmZ88QXdAk5MY'
    access_token = '1031160326744461312-xCI9duv2N6p0ht7baTc8CUR6xBIDj2'
    access_token_secret = '6stUZPZacocjKlbcmDysHeaqafmtQHHPTmNLeIFSuJjVA'
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication Failed")

    app.debug = True
    app.run(host='localhost')
