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

reddit = praw.Reddit(
	client_id="CLIENT_ID",
	client_secret="CLIENT_SECRET",
	password="PASSWORD",
	user_agent="USERAGENT",
	username="USERNAME",
)

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)  # submission url
submission = reddit.submission(id="3g1jfi")  # submission’s ID

try:
	for top_level_comment in submission.comments:
		print(top_level_comment.body)
except AttributeError as ae:
	print(ae)


for top_level_comment in submission.comments:
	if isinstance(top_level_comment, MoreComments):
		continue
	print(top_level_comment.body)
