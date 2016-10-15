#Solved
import re
import math

def isPrime(a):
	if(a < 2): return False
	if(a < 4): return True
	if(a % 6 != 1 and a % 6 != 5): return False
	sq = int(a**0.5) + 1
	n = 6
	while(n-1 <= sq):
		if(a % (n-1) == 0): return False
		if(a % (n+1) == 0): return False
		n += 6
	return True

def isLTP(n):
	n = str(n)
	for x in range(len(n)):
		if(not isPrime(int(n[x:]))):
			return False
	return True

def isRTP(n):
	if(n <= 0): return False
	while(n > 0):
		if(not isPrime(n)):
			return False
		n //= 10
	return True

def isTP(n):
	return isRTP(n) and isLTP(n)


def addR(n):
	L = []
	for x in [1,3,7,9]:
		z = 10*n + x
		if(isRTP(z)):
			L.append(z)
	return L

def addL(n):
	L = []
	for x in range(1,10):
		z = int(str(x)+str(n))
		if(isLTP(z)):
			L.append(z)
	return L

x = [2,3,5,7]
c = 0
while c < len(x):
	a = x[c]
	x += addR(a)
	x = sorted(list(set(x)))
	c += 1
print(sum([a for a in x if(a >= 10 and isTP(a))]))
