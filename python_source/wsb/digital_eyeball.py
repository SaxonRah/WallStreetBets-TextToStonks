from python_source.nlp.spacy_gpu_nlp import spacy_gpu_nlp

import re

import praw
from pprint import pprint

from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
---
Shut the fuck up, I'm working.
Judge me later.
k?
---

https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
"""

# Use a praw.ini file in wsb folder.
# goto https://www.reddit.com/prefs/apps and make an app and update the praw.ini with the information.
# [WallStreetBets-TextToStonks]
# client_id=xxxxxxxxxxxxxx
# client_secret=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
# password=xxxxxxxxxxxxxx
# username=xxxxxxxxxxxxxx

reddit = praw.Reddit("WallStreetBets-TextToStonks",
                     user_agent="Win:WallStreetBets-TextToStonks:0.0 (by /u/DrPixelBits)")
wallstreetbets_subreddit = reddit.subreddit("wallstreetbets")

vader = SentimentIntensityAnalyzer()
parsed_data = []
wallstreetbets = {}

# for submission in reddit.subreddit("wallstreetbets").top("all"):
for submission in reddit.subreddit("wallstreetbets").hot(limit=5):
    wallstreetbets[submission] = {}
    wallstreetbets[submission]['url'] = submission.url
    wallstreetbets[submission]['upvote_ratio'] = submission.upvote_ratio
    wallstreetbets[submission]['score'] = submission.score
    wallstreetbets[submission]['num_comments'] = submission.num_comments
    wallstreetbets[submission]['stickied'] = submission.stickied
    wallstreetbets[submission]['author'] = submission.author.name
    wallstreetbets[submission]['created_utc'] = submission.author.created_utc
    wallstreetbets[submission]['title'] = submission.title
    wallstreetbets[submission]['title_ne_p_and_c'] = spacy_gpu_nlp(wallstreetbets[submission]['title'])

    wallstreetbets[submission]['author_polarity'] = vader.polarity_scores(wallstreetbets[submission]['author'])
    wallstreetbets[submission]['title_polarity'] = vader.polarity_scores(wallstreetbets[submission]['title'])

    pattern = r'(\$)[a-zA-Z.]+'
    title_ticker_result = re.findall(pattern, wallstreetbets[submission]['title'])
    selftext_ticker_result = ''

    if submission.is_self:
        wallstreetbets[submission]['selftext'] = submission.selftext
        wallstreetbets[submission]['selftext_ne_p_and_c'] = spacy_gpu_nlp(wallstreetbets[submission]['selftext'])
        wallstreetbets[submission]['selftext_polarity'] = vader.polarity_scores(wallstreetbets[submission]['selftext'])

        selftext_ticker_result = re.findall(pattern, wallstreetbets[submission]['selftext'])

    if title_ticker_result and not selftext_ticker_result:
        ticker = title_ticker_result
    elif selftext_ticker_result and not title_ticker_result:
        ticker = selftext_ticker_result
    elif title_ticker_result and selftext_ticker_result:
        ticker = title_ticker_result + selftext_ticker_result
    else:
        ticker = 'No Ticker Found.'
pprint(wallstreetbets)

# Generate new Graph for Reddit Posts without pandas, lets reduce some dependencies for now.

# Can combine subreddits.
# for submission in reddit.subreddit("wallstreetbets+stocks").top("all"):
#    print(submission)

# Example Shit
# url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
# submission = reddit.submission(url=url)  # submission url
# submission = reddit.submission(id="3g1jfi")  # submission’s ID
# try:
#     for top_level_comment in submission.comments:
#         print(top_level_comment.body)
# except AttributeError as ae:
#     print(ae)
# for top_level_comment in submission.comments:
#     if isinstance(top_level_comment, MoreComments):
#         continue
#     print(top_level_comment.body)
