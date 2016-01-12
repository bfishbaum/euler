#Solved
import prime
def distPrimes(x):
	return len(list(set(prime.primeFactors(x))))

done = False
length = 0
i = 2
while(not done):
	i += 1
	if(distPrimes(i) == 4):
		print(i)
		length += 1
		if(length == 4):
			done = True
	else:
		length = 0
print(i)
