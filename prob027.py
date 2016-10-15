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

pSet = set()
aV = [a for a in range(-999,1000)]
bV = [b for b in range(0,999) if isPrime(b)]
values = [(a,b) for a in aV for b in bV]

def value(a,b):
	n = 0
	z = n**2 + a*n + b
	while z in pSet or isPrime(z):
		pSet.add(n**2+a*n+b)
		n += 1
		z = n**2 + a*n + b
	return n

m = max(values,key=lambda x: value(x[0],x[1]))
print(m[0]*m[1])
