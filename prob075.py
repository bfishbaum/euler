#Solved
import time
from math import *
def gcd(x,y):
	while(x != 0):
		x,y = y%x,x
	return y

def gcd3(a,b,c):
	return gcd(gcd(a,b),c)

def isPyt(a,b,c):
	return a**2 + b**2 == c**2

def isUnqPyt(a,b,c):
	return (isPyt(a,b,c) and gcd3(a,b,c) == 1
			and a > 0 and b > 0 and c > 0)

# generate primitive pythagorean triplet
def genPrim(m,n):
	#based on euclid's formula
	return (2*(m**2 + m*n))

pers = [0] * 1500001

for m in range(1,int(sqrt(len(pers)/2)) + 1):
	for n in range(m%2 + 1,m,2):
		if(gcd(m,n) == 1):
			k = genPrim(m,n)
			for i in range(0,len(pers),k):
				pers[i] += 1

print(pers.count(1))
