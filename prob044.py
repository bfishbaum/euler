#Solved
import math
def qf(a,b,c):
	k = (b**2-4*a*c)
	if(k < 0):
		return 0
	q = math.sqrt(k)
	return (-b + q)/(2*a)

nPent = lambda x: (3*x**2-x)/2

pentD = {1:1}

def isPent(a):
	b = int(qf(3,-1,-2*a))
	return b if nPent(b) == a else -1

found = 8
c = 1
k = 1
while found != 0:
	for x in range(1,c):
		a = pentD[x]
		if(c in pentD):
			b = pentD[c]
		else:
			b = nPent(c)
			pentD[c] = b
		if(isPent(b-a) != -1 and isPent(a+b) != -1):
			print(a,b,b-a,a+b)

			found = 0
			break
	c += 1
	if(c > k):
		print(k)
		k *= 1.3
