# WallStreetBets-TextToStonks
Python, Wall Street Bets, Natural Language Processing, Stock Sentiment

(I know, I know. This fucking repo reads a bit like: https://www.youtube.com/watch?v=1NBfZcNU4O0 just bear with...)

# Rah's Belief Model
Written - JAN-25-2021 - Uses GPU computation
My own idea turned out to be a simple combination of Dumb Money and The Codex's Ideas
but combined with an overall sentiment - a supervised learning or a trainable model.
The Codex used NLTK and Vader for Sentiment but I prefer spacy and spacy-stanza, but to each their own. Will use both and compare results.

# Idea
1. Scrape reddit's r/WallStreetBets. Use NLP to get stonk sentiment. <- YOU WERE HERE
2. Scrape finviz's stock news. Use NLP to get article sentiment. <- YOU WERE HERE
3. Try to avoid sentiment engine downsides by parsing content first then realizing a sentiment. <- YOU ARE HERE
4. Graph a collection of WSB post sentiments. <- YOU ARE HERE
5. Graph a collection of finviz's stock news sentiments. <- YOU WERE HERE
6. GUI for graph exploration.
7. GUI for manual entry of WSB post and finviz's stock news to add new or update sentiments in database.
8. Make a simple overall sentiment for stock [x]. An average of all WSB post sentiments and finviz's stock news sentiments collected.
9. Create an AI to do overall sentiment anylasis based on all WSB post sentiments and finviz's stock news sentiments collected.

# Idea taken from Dumb Money Live's video
https://www.youtube.com/watch?v=pykcaisxB1g
# Idea taken from TheCodex's Video
https://www.youtube.com/watch?v=o-zM8onpQZY

# Graph of Stonk Sentiment from News Headlines.
![alt text](https://github.com/SaxonRah/WallStreetBets-TextToStonks/blob/main/readme_resource/Backchecking_Figure.png?raw=true)
# Bullshit Paint Mockup of Stonk Sentiment Tracker
![alt text](https://github.com/SaxonRah/WallStreetBets-TextToStonks/blob/main/readme_resource/WIP_StonkSentimentTracker_GUI.png?raw=true)

# Spacy, NLTK, praw, sqlite3, pandas, matplotlib, BeautifulSoup4, requests, uh, numpy, other shit probably.
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
# Machine used to build and train
i5-9600k
RTX 2080
32gb Ram

# Contributing
Don't. Not yet, atleast. Let something be finished first. It's just a collection of scripts and ideas. Be paitent.
Everything will be "self_test()"-able, so you can learn how everything is structured. Should be pretty self explainitory if you follow the self_test()'s
