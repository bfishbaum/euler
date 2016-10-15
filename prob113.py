#Solved
import math
def isInc(k):
	return ''.join(sorted(str(k))) == str(k)

def isDec(k):
	return ''.join(sorted(str(k),reverse=True)) == str(k)

incL = {}
for x in range(1,10):
	incL[x] = 1
incL[0] = 0

decL = {}
for x in range(10):
	decL[x] = 1
decL[-1] = -1

def addToIncL(d):
	z = [d[x] for x in range(10)]
	for i in range(10):
		d[i] = sum(z[i:])

def addToDecL(d):
	z = [d[x] for x in range(10)]
	for i in range(1,10):
		d[i] = sum(z[:i+1])
	d[-1] += sum(z)-d[0]

def decIncUnderN(k):
	if(k <= 1):
		return 0
	digs = len(str(k))
	z = 9*(digs-1) + int(str(k)[0])
	a = int(str(k)[0] * (digs))
	if(a >= k):
		return z - 1
	return z

def incUnderN(n):
	total = 0
	for x in range(1,n):
		if(isInc(x)):
			total += 1
	return total

def decUnderN(n):
	total = 0
	for x in range(1,n):
		if(isDec(x)):
			total += 1
	return total

t = 100
for x in range(t-1):
	addToIncL(incL)
	addToDecL(decL)
print(sum(incL.values()) + sum(decL.values()) - decIncUnderN(10**t))
