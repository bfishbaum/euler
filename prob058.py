from math import *
def diagSize(s):
	assert(s % 2 == 1)
	return 2*s-1

def diagNumbers(s):
	assert(s % 2 == 1)
	t = s**2
	L = [t - (s-1)*i for i in range(3,-1,-1) if isPrime(t-(s-1) * i)]
	return len(L)

def isPrime(x):
	if(x < 2): return False
	if(x < 4): return True
	for n in range(2,int(sqrt(x)) + 1):
		if(x % n == 0):
			return False
	return True
		
found = False
s = 1
p = 0
while not found:
	s += 2
	#print(s)
	p += diagNumbers(s)
	d = 2*s-1
	#print(1.0*p/d)
	if(10*p < d):
		found = True
print(s)

