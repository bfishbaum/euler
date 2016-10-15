#Solved
import prime

pList = prime.sieve(1000000)
sumList = [0]
for x in range(len(pList)):
	sumList.append(pList[x]+sumList[-1])
sumSet = set(sumList)

def sumOfConsecutivePrimes(x):
	global sumSet
	global sumList

	for y in sumList:
		if(y-x in sumSet):
			return(x,y)
		if(y > x):
			break
	return False

def lengthOfConsecutivePrimes(x,y):
	global sumList
	index1 = sumList.index(y)
	index2 = sumList[0:index1].index(y-x)
	print(x,index1,index2)
	return index1 - index2

pList = pList[::-1]
maxP = (0,0)
for x in pList:
	length = sumOfConsecutivePrimes(x)
	if(length != False):
		z = lengthOfConsecutivePrimes(length[0],length[1])	
		if z > maxP[1]:
			maxP = (x,z)
	if(x < sumList[maxP[1]]):
		break
	
print(maxP)
