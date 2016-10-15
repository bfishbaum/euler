#Solved
from math import sqrt
def gcd(x,y):
	while(x != 0):
		x,y = y%x,x
	return y	

def genPPT(m,n):
	m2 = m**2
	n2 = n**2
	return m2-n2,2*m*n,m2+n2

def makeAllPPT(k):
	L = []
	for m in range(k):
		for n in range(m%2+1,m,2):
			if(gcd(m,n) == 1):
				a,b,c = genPPT(m,n)
				t = makeIAE(a,b,c)
				if(t != None):
					print(m,n)
					L.append(t)
	return L

def makeIAE(a,b,c):
	if(abs(c-2*a) <= 1):
		return (2*a,c,c)
	if(abs(c-2*b) <= 1):
		return (2*b,c,c)
	return None

L = [(2,1),(4,1),(7,4),(15,4)]
def addToL(L):
	x = L[-1][1]*4 - L[-3][1]
	y1 = L[-2][1] + L[-2][0] + L[-1][0]
	y2 = y1 * 2 + L[-1][1]
	L.append((y1,x))
	L.append((y2,x))

def isIAE(a,b):
	#two sides length a
	#one side length b
	if(a*2 <= b): return False
	if(abs(a-b) > 1): return False
	s = b/2
	if(s > a): return False
	h = sqrt(a**2-s**2)
	if((h * s) % 1 == 0):
		return True
	return False

for x in range(20):
	addToL(L)

total = 0
for k in L:
	a,b,c = genPPT(k[0],k[1])
	t = makeIAE(a,b,c)
	if(sum(t) <= 10**9):
		total += sum(t)
	else:
		print(k)

print(total)
	
