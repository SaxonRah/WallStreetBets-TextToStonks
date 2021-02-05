import sqlite3 as sl

"""

The [x] Relational? Database 	- Key : Value
    Date_Table                  - What date and time is it currently when executing the stonk stonkerton.
        Date_Table_Key		    - 0, 1, ect...
        Date_Table_Value		- year/month/day
        Date_Table_Time         - UTC Time
        
    Ticker_Table
        Ticker_Table_Key		- 0, 1, ect...
        Ticker_Table_Value		- GME, AMC, ect...
        Ticker_Table_Value_Name - 'GameStop Corp.', 'AMC Theatres', ect...

    Sentiment_Table
        Sentiment_Table_Key     - 0, 1, ect...
        Date_Table_Key          - Date and Time when added to databased.
        Ticker_Table_Key        - Ticker_Table_Key (0 (GME), 1 (AMC), ect...)
        Post					- "I think GME will moon." (string)
        Sentiment				- 0 to 1 (integer)

    Overall_Table
        Overall_Table_Key		- Ticker_Table_Key (0 (GME), 1 (AMC), ect...)
        Overall_Sentiment		- 0.0 to 1.0 (decimal)
        Sentiment_Table			- Sentiment_Table_Key (0, 1, ect...)

"""

# Create
connection_handle = sl.connect('wsb-tts-data-based.db')
with connection_handle:
    connection_handle.execute("""
        CREATE TABLE TICKER_TABLE (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            ticker TEXT,
            full_name TEXT
        );""")

# Update
sql = 'INSERT INTO TICKER_TABLE (id, ticker, full_name) values(?, ?, ?)'
data = [
    (1, 'GME', 'GameStop Corp.'),
    (2, 'AMC', 'AMC Theatres'),
    (3, 'BB', 'BlackBerry Limited')
]

with connection_handle:
    connection_handle.executemany(sql, data)

# Select data from based.
with connection_handle:
    data = connection_handle.execute("SELECT * FROM TICKER_TABLE")
    for row in data:
        print(row)
