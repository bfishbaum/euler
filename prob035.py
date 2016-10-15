#Solved
import math
import prime
def rotateDigits(x):
	size = math.floor(math.log(x,10))
	y = x%10
	z = x//10
	return y * 10**size + z

def isCircularPrime(x):
	size = math.floor(math.log(x,10))+1
	for turn in range(size):
		if(not prime.isPrime(x)): return False

		x = rotateDigits(x)
	return True

sum = 0
for n in range(2,1000000):
	if(isCircularPrime(n)):
		sum += 1
		print(n)	
print(sum)
	
	
