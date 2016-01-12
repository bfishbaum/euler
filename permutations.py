import copy
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

def permuteN(L,n):
	a = chooseN(L,n)
	b = []
	for x in a:
		b += permute(x)
	return b

def permute(l):
	L = copy.copy(l)
	result = [[]]
	while(len(L) > 0):
		temp2 = []
		i = L.pop(0)
		for per in result:
			for j in range(len(per)+1):
				newPer = per[:j] + [i] + per[j:]	
				temp2.append(newPer)
		result = temp2
	return result

def nCr(n,r):
	result = 1
	r = max(r,n-r)
	for x in range(r+1,n+1):
		result *= x
	for x in range(1,n-r+1):
		result //= x
	return result

def nPr(n,r):
	result = 1
	for x in range(r+1,n+1):
		result *= x
	return result
