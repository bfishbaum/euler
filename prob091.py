from math import sqrt
def isIAE(k):
	a = k[0]
	b = k[1]
	if(a*2 <= b): return False
	if(abs(b-a) > 1): return False
	s = a/2
	h = sqrt(b**2-s**2)
	if((h * s) % 1 == 0):
		return True
	return False

for x in range(2,1000):
	if(isIAE((x,x-1))):
		print(x,x,x-1)
	if(isIAE((x-1,x))):
		print(x-1,x-1,x)
