#solved
import prime as pi
import time

const = 10**8

def bSearch(G,x):
	z = const/x;
	lo = 0
	hi = len(G);
	if(G[lo] >= z): return -1
	while(lo < hi-1):
		mid = (hi+lo)//2
		if(G[mid] >= z):
			hi = mid
		else:
			lo = mid	
				
	return lo

L = pi.sieve(const//2)
total = 0

for i in range(len(L)):
	z = bSearch(L[i:],L[i])	
	total += 1 + z
	if(z < 0):
		break
print(total)
