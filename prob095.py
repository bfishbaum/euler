#Solved

import sys
import math
gcd = lambda x,y: y if x == 0 else gcd(y%x,x)
sqrt = lambda x: int(math.ceil(math.sqrt(x)))

def isPrime(n):
	if(n < 2): return False
	if(n < 4): return True
	if(n % 6 != 5 and n % 6 != 1): return False
	for k in range(6,sqrt(n)+1,6):
		if(n % (k+1) == 0): return False
		if(n % (k-1) == 0): return False
	return True


def primesLT(n):
	k = [False,False] + [True] * (n-1)
	for x in range(0, sqrt(n) + 1):
		if(k[x]):
			for a in range(2*x,n+1,x):
				k[a] = False
	return [x for x in range(2,n+1) if k[x]]

primes = primesLT(10**6)
pSet = set(primes)

d = dict()
def div(n):
	o = n
	if(o not in d):
		t = 1
		if(n in pSet):
			d[o] = o+1
			return d[o]
		for p in primes:
			k = 1
			while(n % p == 0):
				n /= p
				k += 1
			if(n == 1):
				d[o] = ((p**k)-1)/(p-1)
				return d[o]
			if(o/n in d and n in d and gcd(n,o/n) == 1):
				d[o] = d[o/n] * d[n]
				return d[o]
		d[o] = t
	return d[o]

def chainLength(k):
	count = 0
	o = k
	seen = set()
	while(k != 0 and k <= 10**6 and (k not in seen or count == 0)):
		seen.add(k)
		k = d.get(k,6+k)-k
		count += 1
	return count if k == o else 0


#generate all the values
c = 1
for x in range(1,1000000):
	if(x >= c):
		c *= 2
	a = div(x)


################################################################################
m = (0,0)
for x in range(1000000):
	p = chainLength(x)
	if(p > m[0]):
		m = (p,x)
print(m)





