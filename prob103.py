import copy
def sumSet(L):
	j = [0]
	for l in L:
		z = copy.copy(j)
		for i in z:
			j.append(i+l)
	return j

def isSSS(L):
	j = [(0,0)]
	sumSet = set([0])
	for l in L:
		z = copy.copy(j)
		for i in z:
			b = i[0]+l
			if(b in sumSet): return False
			sumSet.add(b)
			j.append((b,i[1]+1))
	return j
