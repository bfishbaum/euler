#Solved
import math
import prime

def replaceDigits(num,digit):
	return int(num.replace("x",str(digit)))


sieve = set(prime.sieve(5000000))
def testDigitCombination(x):
	tot = 0
	startIndex = 0
	if(x.startswith("x")):
		startIndex = 1
	for i in range(startIndex,10):
		newNum = replaceDigits(x,i)
		if(newNum in sieve):
			tot += 1
	return tot == 8

def createCombos(num,inserts):
	digits = math.floor(math.log(num,10))
	num = str(num)
	places = chooseN([x for x in range(digits + inserts)],inserts)
	newStrs = []
	for com in places:
		newString = ""
		temp = num[0:-1]
		for i in range(digits+inserts):
			if(i in com):
				newString += "x"
			else:
				try: newString += temp[0]
				except: pass
				temp = temp[1:]
		newStrs.append(''.join(newString) + num[-1])
	return list(set(newStrs))
	
def chooseN(L,n):
	result = []
	temp1 = [[]]
	while(len(L) > 0):
		i = L.pop()
		temp2 = []
		for j in temp1:
			temp2.append(j)
			if(len(j) == n-1):
				result.append(j + [i])
			else:
				temp2.append(j + [i])
		temp1 = temp2
	return result

for x in range(1,10000):
	for j in range(1,7):
		b = createCombos(x,j)
		for a in b:
			if(testDigitCombination(a)):
				print(a,x)
