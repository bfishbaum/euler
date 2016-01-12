#Solved
import prime as pi

def isPandigital(x):
	x = str(x)
	for c in range(1,len(x)+1):
		if(x.count(str(c)) != 1):	
			return False
	return True

x = pi.sieve(10000000)[::-1]
for y in x:
	if(isPandigital(y)):
		print(y)
		break
