#Solved

def isPrime(n):
	if(n <= 1):
		return False
	elif(n <= 3):
		return True
	elif(n % 6 != 1 and n % 6 != 5):
		return False
	else:
		for x in range(6,int(n**0.5),6):
			if(n % x+1 == 0):
				return False
			if(n % x-1 == 0):
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

def sumPrimes(x):
	primes = primesInRange(x)
	if(primes == []):
		return 0

	def sumFromArray(a,numList):
		if(a == 0):
			return 1
		elif(len(numList) <= 0):
			return 0
		elif(a < numList[0]):
			return 0
		sum = 0
		for i in range(a//numList[0]+1):
			sum += sumFromArray(a-numList[0]*i,numList[1:])
		return sum

	return sumFromArray(x,primes)

i = 0
done = False
while(not done):
	i += 1
	x = sumPrimes(i)
	if(x >= 5000):
		done = True
print(i)
			
	
	
