import prime as pi
import permutations as pr
import math
import time


def confirmList(x):
	x = x[:]
	if(x == []): return False
	if(len(x) == 1): return pi.isPrime(x[0])
	b = x[-1]
	for a in x[:-1]:
		p1 = (a * 10 ** (int(math.log(b,10))+1) + b)
		p2 = (b * 10 ** (int(math.log(a,10))+1) + a)
		if(not pi.isPrime(p1) or not pi.isPrime(p2)):
			return False
	return True

def findPrimeCatSet(high,length):
	final = []
	for j in range(1,3):
		sieve = pi.sieve(high)
		mod1 = [3] + [i for i in sieve if i % 3 == j]
		result = [[i] for i in mod1]
		leng = length
		
		while(leng > 1):
			temp = []
			a = len(result)
			b = 1
			for y in result:
				print(b,a)
				b += 1
				for x in mod1:
					if(x > y[-1]):
						z = y + [x]
						if(confirmList(z)):
							temp += [z]
							
			result = temp
			leng -= 1
			print(len(result))
		final += result
		print(result)
	return final
print([sum(x) for x in [[7, 1237, 2341, 12409, 18433], [13, 5197, 5701, 6733, 8389]]])
x = 1/0
r = findPrimeCatSet(20000,5)
print(r)

