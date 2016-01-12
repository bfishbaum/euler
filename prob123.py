#Solved
import prime as pi
import math
def exp(a,b,modulus):
	tempA = a
	total = 1
	while b > 0:
		log = math.ceil(math.log(modulus,tempA))
		total *= tempA ** (b%log) 
		tempA = (tempA ** log) % modulus
		b //= log
	return total % modulus

sieve = pi.sieve(1000000)
print(sieve[0])
y = 0
for x in range(len(sieve)):
	if(sieve[x] > 10**5):
		y = x
		if(x % 2):
			y -= 1
			break

log = 2
for x in range(2,len(sieve)):
	p = sieve[x-1]
	mod = p**2
	a = exp(p-1,x,mod)
	b = exp(p+1,x,mod)
	r = (a+b) % mod
	if(r > 10**10):
		print(x,"Done")
		break
	if(x > log):
		print(log)
		log *= 2
