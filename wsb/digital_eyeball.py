import praw
from praw.models import MoreComments

"""
---
Shut the fuck up, I'm working.
Judge me later.
k?
---

https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
"""

# Use praw.ini file
# goto https://www.reddit.com/prefs/apps and make an app and update the praw.ini with the information.
# [WallStreetBets-TextToStonks]
# client_id=xxxxxxxxxxxxxx
# client_secret=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
# password=xxxxxxxxxxxxxx
# username=xxxxxxxxxxxxxx

reddit = praw.Reddit("WallStreetBets-TextToStonks",
                     user_agent="Win:WallStreetBets-TextToStonks:0.0 (by /u/DrPixelBits)")
wallstreetbets_subreddit = reddit.subreddit("wallstreetbets")

# for submission in reddit.subreddit("wallstreetbets").hot(limit=25):
for submission in reddit.subreddit("wallstreetbets").top("all"):
    print(submission.title)

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
