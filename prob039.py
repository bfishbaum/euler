#Solved
from math import *
gcd = lambda x,y: y if x == 0 else gcd(y%x,x)

def gcd3(a,b,c):
	return gcd(gcd(a,b),c)

def isPyt(a,b,c):
	return a**2 + b**2 == c**2

def isUnqPyt(a,b,c):
	return (isPyt(a,b,c) and gcd3(a,b,c) == 1
			and a > 0 and b > 0 and c > 0)
			#ensures all positive and ordering
			#prevents duplicates

def makeUnqPyts(per):
	L = set()
	for x in range(1,per-1//2):
		p = per
		if(x != per):
			n = 2*(x**2) + p**2 - 2*p*x
			d = -2*(x-p)
			if(n % d == 0):
				a = x
				b = n//d
				c = p-a-b
				[a,b,c] = sorted([a,b,c])
				if(b > c):
					b,c = c,b
				if(isUnqPyt(a,b,c)):
					L.add((a,b,c))
	return list(L)

def totalPyts(per,d):
	total = 0
	for x in range(1,per+1):
		if(per % x == 0):
			if(per//x in d):	
				total += d[per//x]
			else:
				a = makeUnqPyts(x) 
				d[per//x] = a
				total += a
	return total

d = dict()
t = 1001
for x in range(1,t):
	d[x] = len(makeUnqPyts(x))
print('here')

print(max([(b,totalPyts(b,d)) for b in range(1,t)],key=lambda x:x[1]))
