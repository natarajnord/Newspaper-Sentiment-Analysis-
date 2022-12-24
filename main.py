import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

#API key from newsAPI
api_key = "953b30e0f8c84cb0a7a67fdbeced1599"

# Setting up the API endpoint URL and parameters
api_endpoint = "https://newsapi.org/v2/top-headlines"
params = {
    "apiKey": api_key,
    "language": "en"
}

# Make the API request to retrieve the articles
response = requests.get(api_endpoint, params=params)

#extracting list of articles
articles = response.json()["articles"]

# Initialize the sentiment analyzer variable
sentiment_analyzer = SentimentIntensityAnalyzer()
i=1

for article in articles:
    text = article["description"]

    #classify sentiment of text
    sentiment = sentiment_analyzer.polarity_scores(text)
    print("Article No: {}: {}".format(i,article['description']))
    print("-> Positive : {}% , Negative : {}% , Neutral : {}%.".format(sentiment['pos'] * 100, sentiment['neg'] * 100, sentiment['neu'] * 100))
    print("\n\n")
    i+=1
