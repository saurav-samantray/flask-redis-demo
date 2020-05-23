from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
#TODO

@app.route('/')
def hello():
    redis.incr('hits')
    return render_template('index.html',hits=redis.get('hits').decode("utf-8"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)