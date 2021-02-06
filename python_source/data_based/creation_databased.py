import sqlite3 as sl
import datetime

"""

The [x] Relational? Database 	- Key : Value

    DATETIME_TABLE              - What datetime article or post was made.
        id              	    - 0, 1, ect...
        datetime            	- year/month/day UTC Time in ISO8601 string format YYYY-MM-DD HH:MM:SS.SSS
                
    Ticker_Table
        id              		- 0, 1, ect...
        ticker          		- GME, AMC, ect...
        full_name               - 'GameStop Corp.', 'AMC Theatres', ect...

    Sentiment_Table
        id                      - 0, 1, ect...
        datetime_id             - What datetime article or post was made.
        ticker_id               - What ticker are we processing.
        post					- Post/Article Content
        sentiment				- -1.0 to +1.0

    Overall_Table
        id                      - 0, 1, ect...
        ticker_id               - What ticker are we processing.
        overall_sentiment		- -1.0 to +1.0
        sentiment_list			- sentiment id list ( example: '[0, 2, 3, 5]' )

"""

# Create
connection_handle = sl.connect('wsb-tts-data-based.db')
with connection_handle:

    connection_handle.execute("""
        CREATE TABLE DATETIME_TABLE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            datetime timestamp
        );""")

    connection_handle.execute("""
        CREATE TABLE TICKER_TABLE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            full_name TEXT
        );""")

    connection_handle.execute("""
        CREATE TABLE SENTIMENT_TABLE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            datetime_id integer NOT NULL,
            ticker_id integer NOT NULL,
            post TEXT,
            sentiment REAL,
            FOREIGN KEY (datetime_id) REFERENCES DATETIME_TABLE (id),
            FOREIGN KEY (ticker_id) REFERENCES TICKER_TABLE (id)
        );""")

    connection_handle.execute("""
        CREATE TABLE OVERALL_TABLE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ticker_id integer NOT NULL,
            sentiment_list TEXT,
            sentiment REAL,
            FOREIGN KEY (ticker_id) REFERENCES TICKER_TABLE (id)
        );""")

# Update
datetime_now = datetime.datetime.now()
datetime_now2 = datetime.datetime.now()
datetime_now3 = datetime.datetime.now()
datetime_sql = 'INSERT INTO DATETIME_TABLE (id, datetime) values(?, ?)'
datetime_data = [
    (1, datetime_now),
    (2, datetime_now2),
    (3, datetime_now3)]
with connection_handle:
    connection_handle.executemany(datetime_sql, datetime_data)

# Update
ticker_sql = 'INSERT INTO TICKER_TABLE (id, ticker, full_name) values(?, ?, ?)'
ticker_data = [
    (1, 'GME', 'GameStop Corp.'),
    (2, 'AMC', 'AMC Theatres'),
    (3, 'BB', 'BlackBerry Limited')]
with connection_handle:
    connection_handle.executemany(ticker_sql, ticker_data)

# Update
sentiment_sql = 'INSERT INTO SENTIMENT_TABLE (id, datetime_id, ticker_id, post, sentiment) values(?, ?, ?, ?, ?)'
sentiment_data = [
    (1, 1, 1, 'GME WILL MOON', 1.0),
    (2, 2, 2, 'AMC WILL DIVE', -1.0),
    (3, 2, 2, 'AMC WILL CRASH', -1.0),
    (4, 3, 3, 'BB WILL MOON', 0.5)]
with connection_handle:
    connection_handle.executemany(sentiment_sql, sentiment_data)

# Update
sentiment_sql = 'INSERT INTO OVERALL_TABLE (id, ticker_id, sentiment_list, sentiment) values(?, ?, ?, ?)'
sentiment_data = [
    (1, 1, '[1]', 1.0),
    (2, 2, '[2, 3]', -1),
    (3, 3, '[4]', 0.5)]
with connection_handle:
    connection_handle.executemany(sentiment_sql, sentiment_data)

# Select data from based.
with connection_handle:
    data = connection_handle.execute("SELECT * FROM DATETIME_TABLE")
    for row in data:
        print(row)

# Select data from based.
with connection_handle:
    data = connection_handle.execute("SELECT * FROM TICKER_TABLE")
    for row in data:
        print(row)

# Select data from based.
with connection_handle:
    data = connection_handle.execute("SELECT * FROM SENTIMENT_TABLE")
    for row in data:
        print(row)

# Select data from based.
with connection_handle:
    data = connection_handle.execute("SELECT * FROM OVERALL_TABLE")
    for row in data:
        print(row)
