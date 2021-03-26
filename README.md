# Sentiment Analysis - Natural Language Processing of Tweets
## Prerequisites
1. [Must] Python 3, preferably Python 3.6.5
2. [GoodToKnow] Basic understanding of how to use NLTK
## Introduction

This project is following the Digital Ocean tutorial called [How To Perform Sentiment Analysis in Python 3 Using the Natural Language Toolkit (NLTK)](https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk).

This project is designed to take unstructured data (such as Social Media posts, News Articles, and Search History) and performing sentiment analysis, which is the classification of texts or parts of texts into pre-defined sentiments.
To achieve this, I will be using Natural Language Toolkit (NLTK), a Natural Language Processing library for Python.

In this project, I will:
1. Prepare a dataset of sample tweets provided by NLTK with different data cleaning methods
2. Train a model on pre-classified tweets
3. Use the model to classify the sample tweets into Negative and Positive Sentiment

- [Step 1 - Tokenisation](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B1%5Dnlp_tokenise.py)
- [Step 2 - Normalisation](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B2%5Dnlp_normalise.py)
- [Step 3 - Noise Removal](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B3%5Dnlp_remove_noise.py)
- [Step 4 - Determine Word Density](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B4%5Dnlp_determine_word_density.py)
- [Step 5 - Prepare Model Data](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B5%5Dnlp_prepare_model_data.py)
- [Step 6 - Build Model And Test](https://github.com/SamuelBridges/SentimentAnalysisTutorial/blob/master/Steps/%5B6%5Dnlp_build_and_test.py)

## Expected Results
![Results](https://raw.githubusercontent.com/SamuelBridges/SentimentAnalysisTutorial/master/test_image.JPG)


## Test The Sentiment Analysis

To use SentimentAnalysis.py, download the file then install the required modules as such:

`$ py`

```python
>>> import nltk
>>> nltk.download('twitter_samples')
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('stopwords')
```

Then from shell run `$ python SentimentAnalysis.py` and input a tweet to check the sentiment.

![Example](https://raw.githubusercontent.com/SamuelBridges/SentimentAnalysisTutorial/master/example_usage.JPG)