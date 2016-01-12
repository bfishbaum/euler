#Solved
import math
import time
def isReversible(x):
	b = 0
	a = x
	while(x != 0):
		b *= 10
		b += x%10
		x //= 10
	total = a + b
	while(total != 0):
		if(not total % 2): return False	
		total //= 10
	return True

def isReversible2(x):
	set1 = set("13579")
	for c in str(x+int(str(x)[::-1])):
		if(c not in set1): return False
	return True

def listBinary(num):
	result = []
	for i in range(num):
		s = ""
		a = math.ceil(math.log(num,2))-1
		for j in range(a,-1,-1):
			s += str(i // (2**j) % 2)
		for x in range(2**(math.ceil(len(s)/2))):
			s10 = ""
			for y in range(math.ceil(len(s)/2)-1,-1,-1):
				s10 += str(x // (2**y) % 2)
			result.append((s,mirrorString(s10,not len(s)%2)))
	return result

def mirrorString(s,mirrorMiddle):
	s2 = s[::-1]
	return s + mirrorMiddle*(s2[0]) + s2[1:]

def isRevBi(s,s10):
	a = int(s)
	b = int(s[::-1])
	c = a+b + 10 * int(s10)
	set1 = set("13579")
	for x in str(c):
		if(x not in set1):
			return False
	return True
		
def pairCounts():
	result = [0 for x in range(8)]
	for x in range(100):
		index = 0
		a = x//10
		b = x%10
		if(a % 2): index += 1	
		if(b % 2): index += 2
		if(a+b >= 10): index += 4
		result[index] += 1
	return result
			
#into the number of reversible numbers it represents
mult = pairCounts()
print(mult)
def convert(s,s10):
	global mult
	if(not isRevBi(s,s10)):
		return 0
	else:
		total = 1
		for x in range(0,len(s)//2):
			a,b,c = int(s[x]),int(s[-x-1]),int(s10[x])
			index = 0
			if(a): index += 1	
			if(b): index += 2
			if(c): index += 4
			if(x != 0): total *= mult[index]
			else:
				total *= [0,10,10,0,0,10,10,0][index]
		if(len(s) % 2 == 1):
			a = int(s[len(s)//2])
			c = int(s10[len(s)//2])
			if(a and c):
				total *= 3
			elif(a or c):
				total *= 2
			else:
				total *= 3
		return total

def numberOfReverse(n):
	sum = 0
	for x in range(1,n+1):
		numbers = listBinary(2**x)
		for i in numbers:
			a = convert(i[0],i[1])
			if(a):
				sum += a
	return sum
		
print(numberOfReverse(12))

#total = 0
#tot1 = 0
#log = 10
#counter = 1
#time1 = time.time()
#for x in range(1,10000001):
#	if(x % 10 != 0):
#		if(isReversible2(x)):
#			total += 1
#	if(x >= log):
#		counter += 1
#		print(log, total,end="|")
#		print(log, numberOfReverse(counter))
#		tot1 = total
#		log *= 10
#time2 = time.time()
#print(time2-time1)
