import numpy as np
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

def sumxy(min, max):
    if min >= max:
        return null
    sum = np.random.randint(min, max)
    y = np.random.randint(1, sum)
    x = sum - y
    return [x, y, sum, abs(x - y)]


@app.route('/question/sum')
def post_question_sum():
    return jsonify({
        "result": sumxy(20, 50)
    })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our Intelligent App!!</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
        
