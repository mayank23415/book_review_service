import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def get_books_cache():
    data = r.get("books")
    if data:
        return json.loads(data)
    return None

def set_books_cache(books):
    r.set("books", json.dumps(books), ex=60)  # expires in 60 seconds
