#Solved
import prime
sieve = prime.sieve(100)
sieve2 = sieve[0:-1]

def product(L):
	i = 0
	prod = 1
	while(i < len(L)):
		prod *= L[i]
		i += 1
	return prod

def totRatio(L):
	totList = [x-1 for x in L]
	return product(L)/product(totList)

l = [sieve2.pop(0) for x in range(5)]
print(sieve2[0])
while(product(l) < 100000):
	l.append(sieve2.pop(0))
	print(totRatio(l),product(l))
