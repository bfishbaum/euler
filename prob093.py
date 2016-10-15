#Solved
import permutations as pr
import copy

def expr(a,b,oper):
	try:
		if(oper == 0):
			return a+b
		elif(oper == 1):
			return a-b
		elif(oper == 2):
			return a*b
		elif(oper == 3):
			return a/b
	except: pass
	return None

def solveAllWays(e):
	result = []
	for k in range(6):
		try:
			x = k % 3
			y = k // 3
			i1 = x * 2
			i2 = y * 2
			(a1,o1,b1) = e[i1:i1+3]
			e1 = e[:i1] + [expr(a1,b1,o1)] + e[i1+3:]
			(a2,o2,b2) = e1[i2:i2+3]
			e2 = e1[:i2] + [expr(a2,b2,o2)] + e1[i2+3:]
			(a3,o3,b3) = e2
			result.append(expr(a3,b3,o3))
		except:
			pass
	return result

def solveExpr(e):
	while(len(e) > 1):
		(a,o,b) = e[:3]
		e = [expr(a,b,o)] + e[3:]
	return e[0]

def addAllOpers(e):
	result = []
	for x in range((len(e)-1)**4):
		l = []
		for y in range(len(e)-2,-1,-1):
			l.append((x//(4**y)) % 4)
		result.append(interleave(e,l))
	return result
		
def interleave(a,b):
	a, b = a[:], b[:]
	result = []
	while(a != [] and b != []):
		result.append(a.pop(0))
		result.append(b.pop(0))
	return result + a + b

def cleanList(total):
	total = list(set(total))
	total = [int(x) for x in total if x != None and x % 1 == 0 and x > 0]
	total.sort()
	for x in range(1,len(total)+1):
		if(total[x-1] != x):
			return x-1 
	return len(total)-1

def totalRange(e):
	ways = pr.permute(e)
	total = []
	for way in ways:
		y = addAllOpers(way)
		for z in y:
			total += solveAllWays(z)
	return cleanList(total)

digs = [x for x in range(10)]
combos = pr.chooseN(digs,4)
max = 0
maxE = None
for c in combos:
	x = totalRange(c)
	print(x)
	if x > max:
		max = x
		maxE = c
print(max,maxE)
