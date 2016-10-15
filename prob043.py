#Solved
import itertools
def isK(x):
	L = [2,3,5,7,11,13,17]
	for i in range(1,8):
		k = (x//(10**(7-i))) % 1000
		if(k % L[i-1] != 0):
			return False
	return True

j = itertools.permutations([str(x) for x in [1,2,3,4,5,6,7,8,9,0]],10)
s = 0
for a in j:
	i = int(''.join(a))
	if(isK(i)):
		s += i
print(s)
