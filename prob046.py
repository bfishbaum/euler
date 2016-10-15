#Solved
import prime

sieve = set(prime.sieve(10000)[1:])
squares2 = [2*x**2 for x in range(1,100)]
def goldbach(z):
	if(z in sieve):
		return True
	for x in squares2:
		if(x > z):
			print(x,z)
			return False
		elif(z-x in sieve):
			return True
	else:
		print(x,z)
		return False
		

for x in range(9,10000,2):
	if(not goldbach(x)):
		print(x)
		break
	
	
	

