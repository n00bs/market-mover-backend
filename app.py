import os
import redis
from flask import Flask

app = Flask(__name__)
#cache = redis.from_url(os.environ.get("REDIS_URL"))
#redis://default:FEp8Ddi2Pj73KkIxl01Kz9zRyLhPfkhK@redis-19690.c92.us-east-1-3.ec2.cloud.redislabs.com:19690
cache = "redis://default:FEp8Ddi2Pj73KkIxl01Kz9zRyLhPfkhK@redis-19690.c92.us-east-1-3.ec2.cloud.redislabs.com:19690"

@app.route('/')
def get_cache():
    return cache.get('stonks') or "No job data saved."

@app.route('/upload/<data>')
def set_cache(data):
    cache.set('stonks-', data)
    return "Job data saved."

if __name__ == '__main__':
    app.run(debug=True)
