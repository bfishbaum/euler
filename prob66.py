#Solved
def solveDioEq(d):
	i = 0
	best = (0,0)
	while(i < 100):
		i += 1
		a = reduce(contFraction(sqrContFraction(d,i)))
		if(assertEq(a[0],a[1],d)):
			if a[0] < best[0] or best[0] == 0:
				best = a
	i = 0
	while(i < 10):
		i += 1
		a = sqrtNewton(d,i)
		if(assertEq(a[0],a[1],d)):
			if a[0] < best[0] or best[0] == 0:
				best = a
	if(best[0] == 0): return None
	
	return best


def assertEq(x,y,d):
	return x**2-d*y**2 == 1

def solveDioEqSlow(d):
	a = solveDioEq(d)
	if(a == None): return None
	i = 0
	return a
	while(i < a[0]):
		i += 1
		if (i**2*d+1)**0.5 % 1 == 0:
			return ((i**2*d+1)**0.5,i)
	return a

def contFraction(values):
	frac = (values.pop(),1)
	def addToFrac(fract,add):
		return (fract[0]+add*fract[1],fract[1])
	while(values != []):
		frac = addToFrac(frac[::-1],values.pop())
	return frac
			
def sqrContFraction(n,accuracy):

	def nextIter(num):
		a = int(num[0]**0.5 + num[1]) // num[2]
		# a is the integer part of whats left
		num2 = (num[0], num[1]- a * num[2])
		#subtract it from the rest

		bottom = (num2[0] - num2[1]**2) // num[2]

		top = (num2[0],-num2[1])

		return a,(top[0],top[1],bottom)

	x = int(n**0.5)
	if(x == n**0.5):
		return [x]
	result = [x]
	rest = (n,x,n-x**2)
	orig = rest
	first = False
	i = 0
	while(i < accuracy):
		i += 1
		first = True
		a,rest = nextIter(rest)
		result.append(a)
	return result

def sqrtNewton(x,accuracy):
	if(x**0.5 % 1 == 0):
		return (x**0.5,1)
	guess = (1,1)
	count = 0
	while count < accuracy:
		count += 1
		temp = (x * guess[1],guess[0])
		g = fracAdd(guess,temp)
		guess = reduce((g[0],g[1]*2))
	return guess
		
	
def fracAdd(a,b):
	a,b = (a[0] * b[1],a[1]*b[1]),(b[0] * a[1],b[1]*a[1])
	new = (a[0] + b[0], a[1])
	return reduce(new)

def reduce(a):
	g = gcd(a[0],a[1])
	return (a[0]//g, a[1]//g)

def gcd(x,y):
	while(y != 0):
		x,y = y,x%y
	return x

xList = []
for x in range(1,1001):
	y = solveDioEqSlow(x)
	if(y != None):
		xList.append((y[0],x))
		print("%d^2 - %d*%d^2 = 1" % (y[0],x,y[1]))

print(max(xList,key = lambda x:x[0]))
