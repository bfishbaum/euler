#Solved
import math
def isPandigital(s):
	s = str(s)[:9]
	for x in range(1,10):
		if(s.count(str(x)) != 1):
			return False
	return True

def startEndPan(x):
	x = str(x)
	s1 = x[:9]
	s2 = x[-9:]
	return isPandigital(s1) and isPandigital(s2)

fibDict = {}
def fib(x):
	z = 0
	try:
		z = max(fibDict.keys())
		a = fibDict[z-1]
		b = fibDict[z]
	except:
		a,b = 1,0
	for y in range(x-z):
		a,b = b,a+b
	fibDict[x] = b
	fibDict[x-1] = a
	return b

x = 1
y = 0
counter = 0
while(True):
	x,y = y,x+y
	y %= 10**9
	counter += 1
	if(isPandigital(y)):
		a = fib(counter)
		print(counter)
		if(isPandigital(str(a)[:9])):
			break
			
				
