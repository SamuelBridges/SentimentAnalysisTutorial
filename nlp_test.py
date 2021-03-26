# Requires Natural Language Toolkit
#   pip install nltk==3.3
# From NLTK requires:
#   import nlkt
#   nltk.download('twitter_samples')
#   nltk.download('punkt')
#   nltk.download('wordnet')
#   nltk.download('averaged_perceptron_tagger')

from nltk.tag import pos_tag
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

print(pos_tag(tweet_tokens[0]))