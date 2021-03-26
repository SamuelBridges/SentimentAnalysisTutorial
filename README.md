# Sentiment Analysis - Natural Language Processing of Tweets
## Prerequisites
1. [Must] Python 3, preferably Python 3.6.5
2. [GoodToKnow] Basic understanding of how to use NLTK
## Introduction

This project is a following the Digital Ocean tutorial called [How To Perform Sentiment Analysis in Python 3 Using the Natural Language Toolkit (NLTK)](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk).

This project is designed to take unstructured data (such as Social Media posts, News Articles, and Search History) and performing sentiment analysis, which is the classification of texts or parts of texts into pre-defined sentiments.
To achieve this, I will be using Natural Language Toolkit (NLTK), a Natural Language Processing library for Python.

In this project, I will:
1. Prepare a dataset of sample tweets provided by NLTK with different data cleaning methods
2. Train a model on pre-classified tweets
3. Use the model to classify the sample tweets into Negative and Positive Sentiment

## Step 1 - Installing NLTK and Downloading Data
First, install NLTK and download the sample data

Install NLTK Package using PIP

`$ pip install nltk==3.3`

Import library and download data

`$ py`

```python
>>> import nltk
>>> nltk.download('twitter_samples')
>>> exit()
```

## Step 2 - Tokenising the Data

Tokenising data refers to the act of splitting strings to create small tokens.

A token could be something such as a noun, a verb, hashtags, links, or even emoticons / emojis. Tokenising works by splitting strings on whitespaces or punctuation.

Second, create a new file:

`$ nano nlp_test.py`

Then, import three sets of data to train and test the model

- `negative_tweets.json`: 5000 tweets with negative sentiment
- `positive_tweets.json`: 5000 tweets with positive sentiment
- `tweets.20150430-223406.json`: 20000 tweets with no sentiments

```python
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
```

Before tokenising, a resource called `punkt` will be downloaded. This resource is a pre-trained model which helps to tokenise the words and sentences.

`$ py`

```python
>>> import nltk
>>> nltk.download('punkt)
```

Once downloaded, the tokeniser allows us to use the `.tokenized()` method. The next step is to tokenise the positive tweets.

```python
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
```

In order to see the tokenised list, a print must be added.

```python
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

print(tweet_tokens[0])
```

Then run the python file

`$ py nlp_test.py`

And the following output should be shown

```shell
['#FollowFriday',
 '@France_Inte',
 '@PKuchly57',
 '@Milipol_Paris',
 'for',
 'being',
 'top',
 'engaged',
 'members',
 'in',
 'my',
 'community',
 'this',
 'week',
 ':)']
```

## Step 3 - Normalising the data