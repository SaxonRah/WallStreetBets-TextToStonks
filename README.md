# WallStreetBets-TextToStonks
Python, Wall Street Bets, Natural Language Processing, Stock Sentiment

(I know, I know. This fucking repo reads a bit like: https://www.youtube.com/watch?v=1NBfZcNU4O0 just bear with...)

# Spacy, NLTK, praw, sqlite3, pandas, matplotlib, BeautifulSoup4, requests, uh, numpy, other shit probably.

# Graph of Stonk Sentiment from News Headlines.
![alt text](https://github.com/SaxonRah/WallStreetBets-TextToStonks/blob/main/readme_resource/Backchecking_Figure.png?raw=true)

# Bullshit Paint Mockup of Stonk Sentiment Tracker
![alt text](https://github.com/SaxonRah/WallStreetBets-TextToStonks/blob/main/readme_resource/WIP_StonkSentimentTracker_GUI.png?raw=true)

```
📦python_source
 ┣ 📂belief_model
 ┃ ┣ 📜belief_model.py
 ┃ ┣ 📜sassy_ticker.py
 ┃ ┗ 📜__init__.py
 ┣ 📂data_based
 ┃ ┣ 📜creation_databased.py
 ┃ ┣ 📜wsb-tts-data-based.db
 ┃ ┗ 📜__init__.py
 ┣ 📂nlp
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜spacy_gpu_nlp.py
 ┃ ┗ 📜__init__.py
 ┣ 📂wsb
 ┃ ┣ 📜digital_eyeball.py
 ┃ ┣ 📜praw.ini
 ┃ ┗ 📜__init__.py
 ┗ 📜__init__.py
```

# Rah's Belief Model
Written - JAN-25-2021 - Uses GPU computation
My own idea turned out to be a simple combination of Dumb Money and The Codex's Ideas
but combined with an overall sentiment - a supervised learning or a trainable model.
The Codex used NLTK and Vader for Sentiment but I prefer spacy and spacy-stanza, but to each their own. Will use both and compare results.

# Idea taken from Dumb Money Live's video
https://www.youtube.com/watch?v=pykcaisxB1g
# Idea taken from TheCodex's Video
https://www.youtube.com/watch?v=o-zM8onpQZY

# Idea
Scrape reddit's r/WallStreetBets. Use NLP to get stonk sentiment. Try to avoid sentiment engine downsides.
Reddit API or with BeautifulSoup4 and Selenium. Or build a simple social media API wrapper, for many API.

# Analyze text syntax.
Named entities, Noun phrases, Noun concepts, Verbs, Sentiments

# Post-Analyze Processing
From gathered information, label the data, and let NN learn from supervision.

# Machine used to build and train
i5-9600k
RTX 2080
32gb Ram

# Contributing
Don't. Not yet, atleast. Let something be finished first. It's just a collection of scripts and ideas. Be paitent.
Everything will be "self_test()"-able, so you can learn how everything is structured. Should be pretty self explainitory if you follow the self_test()'s
