from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

# nltk.download()  # Download vader, (just download all)

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['GME', 'AMC', 'BB']

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):

        title_text = row.a.text
        date_data = row.td.text.split(' ')

        if len(date_data) == 1:
            time = date_data[0]
            date = None
        else:
            date = date_data[0]
            time = date_data[1]

        parsed_data.append([ticker, date, time, title_text])

df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

vader = SentimentIntensityAnalyzer()

function = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(function)
df['date'] = pd.to_datetime(df.date).dt.date

plt.figure(figsize=(10, 8))
mean_df = df.groupby(['ticker', 'date']).mean().unstack()
mean_df = mean_df.xs('compound', axis="columns")
mean_df.plot(kind='bar')
plt.show()
