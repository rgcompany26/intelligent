import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

## 1:S

def ask_sumxy():

	return '''Halle dos números enteros tales que la suma sea {} y la diferencia sea {}".'''.format()

def level_sumxy(level):
	min = 2 * level + 3
	max = 5 * level + 15
	return _sumxy(min, max)


def _sumxy(min, max):
	if min < 3 or max - min < 5:
		return None
	sum = np.random.randint(min, max)
	y = np.random.randint(1, min - 1)
	x = sum - y
	return [x, y, sum, abs(x - y)]


## 1:E

## 2:S

def level_multiplesxy(level):
	min = (level + 30)
	max = (3 * level + 30)
	return _multiplesxy(min, max)


# x + y = z
# x = k * y
# y = z / (k + 1)
def _multiplesxy(min, max):
	if min < 30 or min > max:
		return None
	z = np.random.randint(min, max)
	k = np.random.randint(2, 10)
	y = z // (k + 1)
	x = k * y
	return [x, y, x + y, k]

## 2:E

@app.route('/question/sum')
def post_question_sum():
	level = request.args.get('level') if (request.args.get('level')) else 0
	return jsonify({
		"result": level_sumxy(int(level))
	})


# A welcome message to test our server
@app.route('/')
def index():
	return "<h1>Welcome to our Intelligent App!!</h1>"


if __name__ == '__main__':
	app.run(threaded=True, port=5000)
