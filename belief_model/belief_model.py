"""

---
(I'm retarded. HALP.)
I don't pretend to know anything.
If I'm wrong, I'm wrong.
Help me, so that I may learn.
---

I call this a Belief Model and not a Comprehension Model as it's probably not that good.


Belief Model - Probability that a stonk is good or bad.
	Take all [nlp]'s built from all [i]'s these become clean data.
		Generate a Sentiment scale from 0 to 1 (integer)
		Add or Update Database of information.

	Do the same for news, analysts, ect... articles [na] instead of [sp].
	Generate a probability on all calculated Sentiments for an overall Sentiment.
		Maybe in the future build and train a simple NN to generate a less computable probability of an overall belief.
		like have human's read articles and give their own overall belief scores to articles, posts, ect.
		have NN train off human overall belief scores. give NN mostly raw posts to validate.


Digital Eyeball
	Gather information [sp] (stonk post) in some form [x]
		(csv or database, pref db, wanna try mindsdb with postgreSQL, maybe just csv and postgreSQL?).
		for now i'm gonna use sqlite3 as it's built in. see what's up after something is actually working...


Spacy GPU NLP
	Use nlp analysis to gain information [nlp] about [i], update [x] with [nlp].


The [x] Relational? Database 	- Key : Value
	See creation_databased.py


"""
