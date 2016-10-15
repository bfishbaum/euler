#Solved
import math
import time
def polygonalNumber(ngon,index):
	if(ngon < 3): return 0
	else:
		a = index * (index + 1) // 2
		b = (ngon-3) * index * (index-1) // 2
		return a + b

def isPolygonalNumber(x):
	for gon in range(3,9):
		counter = 0
		number = 1
		while(number < x):
			counter += 1
			number = polygonalNumber(counter,gon)
			if(number == x):
				return (counter,gon)
	return (0,0)

def rotateNumber(x,left=False):
	if(not left):
		a = x % 10
		x = x // 10
		pow = math.floor(math.log(x,10)) + 1
		a = a * 10**(pow)
		x = a + x
	else:
		pow = math.floor(math.log(x,10)) + 1
		x2 = x
		x2 *= 10
		x2 //= 10**pow
		x = x%10**(pow-1) * 10 + x2
	return x

def isCyclicList(L):
	newList = [L.pop(0)]
	while(L != []):
		i = 0
		noneFound = True
		while i < len(L):
			if(areCyclic(newList[-1],L[i])):
				newList.append(L.pop(i))
				noneFound = False
				break
			else: i += 1
		if(noneFound):
			return []
	return newList

def isOrderedCyclicList(L):
	for x in range(0,len(L)):
		if(not areCyclic(L[x-1],L[x])):
			return False
	return True

def areCyclic(a,b):
	a1 = a % 100
	bPow = math.floor(math.log(b,10)) + 1
	b1 = b // (10 ** (bPow - 2))
	b2 = b % 100
	aPow = math.floor(math.log(a,10)) + 1
	a2 = a // (10 ** (aPow - 2))
	return a1 == b1 or a2 == b2

def areCyclicRight(a,b):
	a1 = a % 100
	bPow = math.floor(math.log(b,10)) + 1
	b1 = b // (10 ** (bPow - 2))
	return a1 == b1

def areCyclicLeft(a,b):
	b2 = b % 100
	aPow = math.floor(math.log(a,10)) + 1
	a2 = a // (10 ** (aPow - 2))
	return a2 == b2
	

def all4DigitPolys():
	result = []
	for gon in range(3,9):
		i = 0
		num = 0
		ngon = []
		while(num < 10000):
			i += 1
			num = polygonalNumber(gon,i)
			if(num >= 1000 and num <= 9999):
				ngon.append(num)
		result.append(ngon)
	return result

def allCyclicPairs():
	allPairs = []
	polys = all4DigitPolys()
	for i in range(len(polys)):
		others = polys[:i] + polys[i+1:]
		for j in range(len(others)):
			for num1 in polys[i]:
				for num2 in others[j]:
					if(areCyclicRight(num1,num2)):
						index = j + 3
						if(j >= i): index += 1
						if(num1//10 % 10 != 0 and num2//10 % 10 != 0):
							allPairs.append(((i+3,num1),(index,num2)))
	return allPairs

def constructChain():
	pairs = allCyclicPairs()
	def recurse(chain):
		if(chain == []):
			chain = [pair[0],pair[1]]
		if(len(chain) >= 7):
			if(legitChain(chain)):
				return chain
			else:
				return None
		for pair in pairs:
			num1 = chain[-1]
			if(pair[0] == num1 and pair[1] not in chain[1:]):
				chain2 = chain[:]
				chain2.append(pair[1])
				chain3 = recurse(chain2)
				if(chain3 != None):
					return chain3
		return None
	
	for pair in pairs:
		chain1 = recurse([pair[0],pair[1]])
		if(chain1 != None):
			return chain1


def legitChain(chain):
	numSet = set()
	chain2 = chain[:-1]
	for x in chain2:
		if(x[0] in numSet):
			return False
		numSet.add(x[0])
	if(chain[-1][0] in numSet and chain[0] != chain[-1]):
		return False
	return True
	
newSet = [x[1] for x in constructChain()]
print(newSet)
print(sum(newSet[1:]))

