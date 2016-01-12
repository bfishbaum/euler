#Solved
def sumNumbers(x):
	pairDict = {}
	pairSet = set()

	def sumFromArray(a,n):
		if (a,n) in pairSet:
			return pairDict[(a,n)]
		else:
			numList = [i+n for i in range(a-n)]
			if(a == 0):
				return 1
			elif(a < n):
				return 0
			sum = 0
			for i in range(0,a//n+1):
				sum += sumFromArray(a-n*i,n+1)
			pairSet.add((a,n))
			pairDict[(a,n)] = sum
			return sum

	return sumFromArray(x,1)-1

def pirAndGold(x,y):
	return nCr(x+y-1,x-1)

def nCr(n,r):
	if(n<r): return 0
	r = max(r,n-r)
	product = 1
	for x in range(r+1,n+1):
		product *= x
	for x in range(2,n-r+1):
		product //= x
	return product

def factorial(x):
	product = 1
	for y in range(2,x):
		product *= y
	return product

def sumNumbers2(x):
	sum = 0	
	for z in range(x):
		sum += nCr(1,1)
	return sum

x = 100
print(x,sumNumbers(x))
