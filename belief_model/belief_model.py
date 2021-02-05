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
		Maybe in the future build and train a simple NN to generate a non computable probability of an overall belief.


Digital Eyeball
	Gather information [sp] (stonk post) in some form [x]
		(csv or database, pref db, wanna try mindsdb with postgreSQL, maybe just csv and postgreSQL?).


Spacy GPU NLP
	Use nlp analysis to gain information [nlp] about [i], update [x] with [nlp].


The [x] Relational? Database 	- Key : Value

	Ticker_Table
		Ticker_Table_Key		- 0, 1, ect...
		Ticker_Table_Value		- GME, AMC, ect...

	Sentiment_Table
		Sentiment_Table_Key     - 0, 1, ect...
		Ticker_Table_Key        - Ticker_Table_Key (0 (GME), 1 (AMC), ect...)
		Post					- "I think GME will moon." (string)
		Sentiment				- 0 to 1 (integer)

	Overall_Table
		Overall_Table_Key		- Ticker_Table_Key (0 (GME), 1 (AMC), ect...)
		Overall_Sentiment		- 0.0 to 1.0 (decimal)
		Sentiment_Table			- Sentiment_Table_Key (0, 1, ect...)

The overall_Table describes it's belief in the stonk.

"""
