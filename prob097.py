#Solved
import math
def toBin(n):
	k = int(math.log(n,2))
	s = ''
	for x in range(k,-1,-1):
		if(2**x <= n):
			s += '1'
			n -= 2**x
		else:
			s += '0'
	return s

def modEXP(b,e,m):
	j =  toBin(e)
	n = 1
	for c in j:
		n = n**2 % m
		if(c == '1'):
			n *= b
	return n

a = modEXP(2,7830457,10**10)
a *= 28433
a += 1
print(a % (10 ** 10))
