#Solved
def sumSqrDigits(x):
	s = 0
	while(x > 0):
		s += (x%10)**2
		x //= 10
	return s
	

def findEnd(x):
	if(x == 0): return 0
	y = x
	while(y != 89 and y != 1):
		y = sumSqrDigits(y)
	if(y == 89):
		return 1
	else: return 0

def hash1(x):
	return ''.join(sorted(str(x)))

set1 = set()
for x in range(1000):
	if(findEnd(x)):
		set1.add(x)

set2 = set()
set3 = set()
tot = 0
log = 5
for x in range(1,10 ** 7):
	h = hash1(x)
	if(h not in set3):
		if(sumSqrDigits(x) in set1):
			set3.add(h)
			set2.add(h)
			tot += 1
	else:
		if(h in set2):
			tot += 1
	if(x > log):
		print(log)
		log *= 2
print(tot)
