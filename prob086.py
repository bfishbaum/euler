#Solved
from math import sqrt

def allBoxes(a,b):
	c = b//2 + b%2
	return a//2,max(0,a-c+1)

s = 1
k = 3000
M = [0] * 100000
g = 0
while(s < k):
	for t in range(s+1,k):
		r = int(sqrt(2*s*t))
		if(r**2 == 2*s*t):
			a = int(r+s)
			b = int(r+t)
			aS,bS = allBoxes(a,b)			
			M[a] += bS
			M[b] += aS
	s += 1

t = 0
for x in range(len(M)):
	t += M[x]
	if(t > 1000000):
		print(x)
		print(t)
		break
print(sum(M))





