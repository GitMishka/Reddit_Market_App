import praw
import pandas as pd
import time
import psycopg2
import requests
from twilio.rest import Client
import config

conn = psycopg2.connect(
    host=config.pg_host,
    database=config.pg_database,
    user=config.pg_user,
    password=config.pg_password
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS termlog (
        id TEXT PRIMARY KEY,
        term TEXT,
        subreddit text,
        post_time TIMESTAMP
    )
""")

conn.commit()
cur.close()
conn.close()
