import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Table, Column, String, Integer, DateTime, MetaData, insert
from datetime import datetime
import praw

load_dotenv()

#config
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
SUBREDDIT_NAME = os.getenv("SUBREDDIT", "dataengineering")
FETCH_LIMIT = int(os.getenv("FETCH_LIMIT", "20"))
DB_PATH = os.getenv("DB_PATH", "sqlite:///reddit_data.db")

#config


engine = create_engine(DB_PATH)
metadata = MetaData()

raw_posts = Table(
    'raw_posts', metadata,
    Column('id', String, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('score', Integer),
    Column('created_utc', DateTime),
    Column('url', String)
)
metadata.create_all(engine)

def fetch_and_store_reddit_posts():
    reddit = praw.Reddit(
        client_id = REDDIT_CLIENT_ID,
        client_secret = REDDIT_CLIENT_SECRET,
        user_agent = REDDIT_USER_AGENT
    )

    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    posts = [{
            "id":post.id,
            "title": post.title,
            "author": str(post.author),
            "score": post.score,
            "created_utc": datetime.utcfromtimestamp(post.created_utc),
            "url": post.url
        } for post in subreddit.top(limit=FETCH_LIMIT)]

    with engine.begin() as conn:
        for post in posts:
            stmt = insert(raw_posts).prefix_with("OR IGNORE").values(**post)
            conn.execute(stmt)
    print(f"✅ Stored {len(posts)} posts from r/{SUBREDDIT_NAME}")