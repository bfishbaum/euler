#Solved
import prime as pi
import math

def hyperExp(a,b,modulus=None):
	total = a
	totient = pi.totient(modulus)
	for x in range(b-1):
		total = exp(a,total,modulus,totient)
	return total

def exp(a,b,modulus,totient):
		b = b % totient
		tempA = a
		total = 1
		while b > 0:
			log = math.ceil(math.log(modulus,tempA))
			total *= tempA ** (b%log) 
			tempA = (tempA ** log) % modulus
			b //= log
		return total % modulus

print(hyperExp(1777,1855,10**8))
			
			
		
		

		
