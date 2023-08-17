# Twitter-Sentiment-Analysis-RF
The global outbreak of the coronavirus disease COVID-19 has had a significant impact on numerous countries, raising worldwide health concerns. Governments have implemented regulations aimed at curbing the spread of the disease, affecting various aspects of life, including the economy, healthcare, education, and politics. Consequently, it becomes crucial to analyze public sentiments regarding the government's response to COVID-19. In today's context, individuals frequently utilize social media platforms like Twitter to express their opinions and emotions about COVID-19-related topics.

### Objectives
The objective of this project is to investigate the sentiments expressed by individuals from the Philippines on Twitter regarding the COVID-19 preventive measures in the country. This will be achieved through the utilization of the Random Forest Algorithm, which will aid in constructing a machine learning model designed to categorize sentiments as either positive or negative. The integration of natural language processing techniques will facilitate the assessment of Filipino sentiments concerning the COVID-19 response on Twitter. The outcome of this analysis will provide valuable insights on areas of COVID-19 responses that require improvement. 

### Data Collection from Twitter API
The project utilized the Twitter API to retrieve publicly accessible tweets concerning the COVID-19 responses in the Philippines. Over a duration of 909 days, ranging from January 12, 2020, to July 8, 2022, a total of 51,331 data points were procured. The project followed the subsequent steps for Twitter API authentication and executing API requests:

1. Prior to extracting the required data for the model, it is necessary to undergo an authentication process to gain access to Twitter's server. The API will provide the consumer key, consumer secret, access token, and access secret. These credentials will serve to authenticate the Python script, allowing it to request the necessary resources.

consumer_key = ‘xxxxxxxxxxxx’ <br>
consumer_secret = ‘xxxxxxxxxxx’ <br>
access_token =’xxxxxxxxxxxxxx’ <br>
access_secret = ‘xxxxxxxxxxxx’ <br>
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET) <br>
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET) <br>
api = tweepy.API(auth) <br>

4. Once the API token's authenticity has been confirmed, the librarries (Tweepy or Snscrape) enable the retrieval of data through keyword searches, user handles, geolocation, and language specifications. However, this research focused specifically on collecting data from a particular country, namely the Philippines. The project used the geographical location to specify the location of the Philippines: Latitude: 14.589119422692292, Longitude: 121.0263763730469, Radius: 17097.55 KM and the tweets from the following Philippine news sources (userhandle): “@ABSCBNNews”, “@gmanews”, “@cnnphilippines”, and “@inquirerdotnet”.

keywords = '@ABSCBNNews covid' <br>
limit = 10000 <br>
ph = '14.589119422692292, 121.0263763730469, 17097.55 km' <br>
tweets = tweepy.Cursor(api.search_tweets, q=keywords, lang = 'en', geocode = ph, count = 200, tweet_mode = 'extended').items(limit) <br>

3. Following the extraction of tweets, the selected library will provide these tweets in JSON structure. This JSON data will be parsed into a Python object and subsequently transformed into a dataframe using a library called Pandas.

colums = ['Time', 'User', 'Tweet'] <br>
data = [] <br>
for tweet in tweets: <br>
    data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text]) <br>
df = pd.DataFrame(data, columns=colums) <br>

4. Finally, the acquired dataframe will be saved in CSV format, ready to be utilized for sentiment analysis and the training of the model.

df.to_csv('dataset_tweets.csv') <br>
