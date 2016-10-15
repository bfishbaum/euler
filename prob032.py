#Solved
import copy
def isPrime(a):
	if(a < 2): return False
	if(a < 4): return True
	if(a % 6 != 1 and a % 6 != 5): return False
	sq = int(a**0.5) + 1
	n = 6
	while(n-1 <= sq):
		if(a % (n-1) == 0): return False
		if(a % (n+1) == 0): return False
		n += 6
	return True

def permute(L,n):
	allP = []
	if(n == 0 or len(L) == 0):
		return [[]]
	else:
		for x in range(len(L)):
			lC = copy.deepcopy(L)
			a = lC.pop(x)
			allP += [[a] + x for x in permute(lC,n-1)]

	return allP

def isPandig(a,b,c):
	z  = str(a) + str(b) + str(c)
	return ''.join(sorted(z)) == '123456789'

a =([int(''.join(x)) for x in permute(list('123456789'),4)])
prods = [x for x in a if not isPrime(x)]

tot = 0
for p in prods:
	for j in range(1,99):
		if(p % j == 0 and isPandig(p//j,j,p)):
			tot += p
			break
print(tot)
