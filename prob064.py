#Solved
def contFrac(values):
	temp = values.pop()
	while len(values) > 0:
		temp = values.pop() + 1/temp
	return temp

def sqrContFraction(n,accuracy):
	x = int(n**0.5)
	if(x == n**0.5):
		return [x]
	result = [x]
	rest = (n,x,n-x**2)
	orig = rest
	first = False
	while(rest != orig or not first):
		first = True
		a,rest = nextIter(rest)
		result.append(a)
	return result

def nextIter(num):
	a = int(num[0]**0.5 + num[1]) // num[2]
	# a is the integer part of whats left
	num2 = (num[0], num[1]- a * num[2])
	#subtract it from the rest

	bottom = (num2[0] - num2[1]**2) // num[2]

	top = (num2[0],-num2[1])

	return a,(top[0],top[1],bottom)

def almostEqual(a,b):
	epsilon = 10 ** -12
	return abs(a-b) < epsilon
		
total = 0
for x in range(1,10001):
	l = sqrContFraction(x,100)[1:]
	if(len(l) % 2 == 1):
		total += 1
print(total)
