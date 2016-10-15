#Solved
import prime as pi
import permutations as pr
import math
l = 10000
sieve = pi.sieve(l)
sieveSet = set(pi.sieve(100000))
maxP = max(list(sieveSet))

def isPrime(x):
	if(x < maxP+1):
		return x in sieveSet
	elif(x > l ** 8):
		return pi.isPrime(x)
	else:
		index = 0
		p = sieve[0]
		while p**2 <= x:
			if(x % p == 0):
				return False
			index += 1
			p = sieve[index]
		return True

def concat(a,b):
	return a * 10 ** (int(math.log(b,10))+1) + b

match_dict = {}
def isMatch(a,b):
	if(a > b):
		a,b = b,a
	if((a,b) not in match_dict):
		match_dict[(a,b)] =  isPrime(concat(a,b)) and isPrime(concat(b,a))
	return match_dict[(a,b)]

def isLegit(x):
	for i in range(1,len(x)):
		a = x[i]
		b = x[:i]
		for j in b:
			if not isMatch(j,a): return False
	return True

def findList(prev,primes):
	result = prev
	if(len(prev) == 5):
		return prev
	for x in range(len(primes)):
		y = prev + [primes[x]]
		if(isLegit(y)):
			z = findList(y,primes[x+1:])
			if(z != None):
				return z
	return None
#sieve1 = [3] + [i for i in sieve if i % 3 == 1]
print(sum(findList([],sieve)))
