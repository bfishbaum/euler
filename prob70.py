#Solved (poorly)
import prime
import time

def isPermutation(x,y):
	x,y = str(x),str(y)
	for c in x:
		if(x.count(c) != y.count(c)):
			return False
	return True

time1 = time.time()
primeSet = set(prime.sieve(10**7))
totDict = {1:1}
minNumber = 0
minValue = 0
for x in range(2,10**7):
	if(x not in primeSet):
		y = prime.lowestFactor(x)
		if x % (y**2) == 0:
			tot = totDict[x//y]*y
		else:
			tot = totDict[x//y]*(y-1)
		totDict[x] = tot
		if(isPermutation(x,tot)):
			if(tot/x > minValue):
				print(x,tot,x/tot)
				minValue = tot/x
				minNumber = x
	else:
		totDict[x] = x-1
print(time.time()-time1)
