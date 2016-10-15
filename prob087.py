#Solved
import math

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

t = 5*10**7
z = primesLT(sqrt(t))
p2 = [a**2 for a in z if a**2 < t]
p3 = [a**3 for a in z if a**3 < t]
p4 = [a**4 for a in z if a**4 < t]
s = set()
for a in p2:
	for b in p3:
		for c in p4:
			sm = a + b + c
			if(sm < t):
				s.add(a+b+c)
print(len(list(s)))

