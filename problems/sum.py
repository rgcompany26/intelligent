import numpy as np

def ask_sumxy(level):
	ask = level_sumxy(level)
	if ask:
		return [
			'''Halle dos números enteros tales que la suma sea {} y la diferencia sea {}".'''.format(ask[2], ask[3]),
			[ask[0], ask[1]]
		]

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

def ask_multiplesxy(level):
	ask = level_multiplesxy(level)
	if ask:
		return [
			'''La suma de 2 números es {}. Si el mayor es {} veces el menor. Halle el número menor".'''.format(ask[2], ask[3]),
			[ask[0], ask[1]]
		]

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
	# lowest, highest, sum, factor
	return [y, x, x + y, k]

## 2:E

print('level_sumxy')
for i in range(2, 30):
	print(ask_sumxy(i))

print('level_multiplesxy')
for i in range(2, 30):
	print(ask_multiplesxy(i))
