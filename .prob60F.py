import prime as pi
import permutations as pr
import math
import time

def confirmList(x,sieve):
	x = [str(a) for a in x]
	y = x[-1]
	c = max(list(sieve))
	for z in x[:-1]:
		a = int(z+y)
		b = int(y+z)
		if(a not in sieve and a < c) or not pi.isPrime(a):
			return False
		if(b not in sieve and b < c) or not pi.isPrime(b):
			return False
	return True

def isPair(a,b,sieve):
	p1 = (a * 10 ** (int(math.log(b,10))+1) + b)
	p2 = (b * 10 ** (int(math.log(a,10))+1) + a)
	c = max(list(sieve))
	if(p1 > c):
		if(not pi.isPrime(p1)): return False
	else:
		if(p1 not in sieve): return False
	if(p2 > c):
		if(not pi.isPrime(p2)): return False
	else:
		if(p2 not in sieve): return False
	return True

def connectDict(dict1,listLen):
	keys = sorted(dict1.keys())
	final = []

	def numsMatch(result):
		result = sorted(result)
		for x in range(len(result)-1):
			for y in range(x+1,len(result)):
				if(result[y] not in dict1[result[x]]):
					return False
		return True
			
	def recurse(index,result):
		if(len(result) == listLen):
			print(result)
			final.append(result)
			return result
		else:
			for key in range(index,len(keys)):
				if(numsMatch(result+[keys[key]])):
					ans = recurse(index + 1 + key,result + [keys[key]])
			return None

	recurse(0,[])
	return final

sieve = pi.sieve(3000)
primeSet = set(pi.sieve(3))

mod1 = [3]+[x for x in sieve if x % 3 == 1]
dict1 = {}
for x in range(len(mod1)-1):
	for y in range(x+1,len(mod1)):
		if(isPair(mod1[x],mod1[y],primeSet)):
			dict1[mod1[x]] = dict1.get(mod1[x],[]) + [mod1[y]]

time1 = time.time()
x = connectDict(dict1,4)
time2 = time.time()
print(x,time2-time1)
	
mod2 = [3]+[x for x in sieve if x % 3 == 2]
dict2 = {}
for x in range(len(mod2)-1):
	for y in range(x+1,len(mod2)):
		if(isPair(mod2[x],mod2[y],primeSet)):
			dict2[mod2[x]] = dict2.get(mod2[x],[]) + [mod2[y]]

time1 = time.time()
x = connectDict(dict2,4)
time2 = time.time()
print(x,time2-time1)
