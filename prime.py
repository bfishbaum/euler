import time
import math

def primeFactors(y):
	factors = []
	number = y
	done = False
	while(not done):
		done2 = False
		for x in range(2,int(number**0.5)+1):
			if(number % x == 0):
				factors.append(x)
				number = number//x
				done2 = True
				break
		if(not done2):
			factors.append(number)
			done = True
	return factors

def primeFactorsExclusive(y):
	factors = []
	number = y
	done = False
	while(not done):
		done2 = False
		for x in range(2,int(number**0.5)+1):
			if(number % x == 0):
				if(x not in factors):
					factors.append(x)
				number = number//x
				done2 = True
				break
		if(not done2):
			if(number not in factors):
				factors.append(number)
			done = True
	return factors

def getFactors(n):
	if(n < 0):
		return []
	if(n == 1):
		return [1]
	result = []
	for x in range(1,int(n**0.5)+1):
		if(n % x == 0):	
			result += [x]
	result2 = []
	for x in result:
		if(x*x != n and x != 1):
			result2 += [n//x]
		
	return result + result2[::-1]
	

def isPrime(n):
	if(n <= 1):
		return False
	elif(n <= 3):
		return True
	elif(n % 6 != 1 and n % 6 != 5):
		return False
	else:
		for x in range(6,int(n**0.5)+2,6):
			if(n % (x+1) == 0):
				return False
			if(n % (x-1) == 0):
				return False
		return True

def primesInRange(n):
	if(n <= 1):
		return []
	if(n <= 2):
		return [2]
	primes = [2]
	sieve = [x for x in range(2,n+1)]
	while(sieve != []):
		i = 0
		while(i < len(sieve)):
			if(sieve[i] % primes[-1] == 0):
				sieve.pop(i)
			else:
				i += 1
		primes.append(sieve.pop(0))

	return primes

def sieve(x):
	primes = [2]
	sieve = [True for a in range(x+1)]
	sieve[0:2] = [False,False]
	for i in range(int(x**0.5)+1):
		if(sieve[i]):
			for j in range(i**2,x+1,i):
				sieve[j] = False
	newArray = []
	for x in range(len(sieve)):
		if(sieve[x]):
			newArray.append(x)
	return newArray

def nthPrime(n):
	if(n == 1):
		return 2
	if(n == 2):
		return 3
	i = 2
	x = 1
	last = 0
	while(i < n):
		if(isPrime(6*x-1)):
			i += 1
			last = 6*x-1
			if(i == n):
				break
		if(isPrime(6*x+1)):
			last = 6*x+1
			i += 1
		x += 1
	return last

def totient(x):
	if(x == 1): return 1
	factors = primeFactorsExclusive(x)
	product = 1
	for factor in factors:
		product *= (factor - 1)
		x //= factor
	return product*x

def lowestFactor(x):
	if(x % 2 == 0): return 2
	for i in range(3,int(x**0.5)+1,2):
		if(x % i == 0): return i
	return x

def readFile(path):
    with open(path, "rt") as f:
        return f.read()
