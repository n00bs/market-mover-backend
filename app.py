import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.from_url(os.environ.get("REDIS_URL"))

@app.route('/')
def get_cache():
    return cache.get('reddit_job') or "No job data saved."

@app.route('/upload/<data>')
def set_cache():
    cache.set("reddit_job", data)
    return "Job data saved."

if __name__ == '__main__':
    app.run()
