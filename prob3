#Solved
def primeFactors(y):
	factors = []
	maxN = 1
	number = y
	done = False
	while(not done):
		done2 = False
		for x in range(2,int(number**0.5)):
			if(number % x== 0):
				factors.append(x)
				number = number//x
				done2 = True
				break
		if(not done2):
			factors.append(number)
			done = True
	return factors
			
print(greatestPrimeFactor(600851475143))		
