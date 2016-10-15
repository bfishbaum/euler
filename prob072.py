#Solved
import prime
import fraction

# sum of totients from 2 to 10**6

total = 0
primeSet = set(prime.sieve(10**6))
totDict = {1:1}
for x in range(2,10**6+1):
	if(x not in primeSet):
		y = prime.lowestFactor(x)
		if x % (y**2) == 0:
			tot = totDict[x//y]*y
		else:
			tot = totDict[x//y]*(y-1)
		totDict[x] = tot
		total += tot
	else:
		totDict[x] = x-1
		total += x-1

print(total)
