import math
def bin2Dec(a):
	a = str(a)
	tot = 0
	power = 0
	for c in str(a)[::-1]:
		if(c == '1'):
			tot += 2**power
		power += 1
	return str(tot)

def dec2Bin(a):
	a = int(a)
	x = int(math.log(a,2))
	b = ''
	for power in range(x,-1,-1):
		if(2**power <= a):
			b += '1'
			a -= 2**power
		else:
			b += '0'
	return b

def isBinPal(x):
	a = dec2Bin(x)
	return a == a[::-1]

tot = 0
for x in range(1,999):
	a = str(x)
	p1 = a + a[::-1]
	if(isBinPal(p1)):
		tot += int(p1)
	p2 = a[:-1] + a[::-1]
	if(isBinPal(p2)):
		tot += int(p2)
print(tot)
	
