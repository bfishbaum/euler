#Solved
import prime as pi
import permutations as pr
from numpy import prod
import math
def minProSum(k):
	global last
	for i in range(k,2*k):	
		if(isMinProSum(k,i)):
			last = i
			return i
	return 2*k

def isMinProSum(k,n):
	sums = allFactorSums(n)
	if(k < 100):
		x = k
	else:
		x = k//20
	for x in range(k-x,k):
		a = n - x
		k1 = k - x
		if (a,k1) in sums:
			return True
	return False
		
def findProSumFactors(a,num,n,sums):
	# here we need to find num numbers
	# that sum to a
	sums = sums[:]
	b = n-a
	sum1 = sum(factors)
	while(sum1 < b):
		z = b-sum1
		for pair in factorPairs:
			s1 = sum(pair)
			s2 = prod(pair)
			if(s2-s1 == z):
				return True
	return False

dict1 = {}
def allFactorSums(x):
	if(x not in dict1):
		if(pi.isPrime(x)):
			return [(x,1)]
		else:
			total1 = []
			facts = pi.getFactors(x)[1:]
			for i in facts:
				for j in allFactorSums(x//i):
					total1.append((i+j[0],1+j[1]))
					total1.append((i+x//i,2))
		dict1[x] = frozenset(total1)
	return dict1[x]

set1 = set()	
log = 2
for k in range(2,12001):
	t = minProSum(k)
	print(k,t)
	set1.add(t)
	if(k > log):
		print(log)
		log = int(log*1.5)

print(sum(list(set1)))
	
