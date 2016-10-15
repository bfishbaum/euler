import math
def works(b,r):
	n = (2*(b**2) - (2*b)) + (b+r)
	m = (b+r)**2 - (b+r) + (b+r)
	a = 2*(b)*(b-1) + (b+r)
	z = 2*(b)*(b-1)
	c = (b+r)*(b+r-1)
	print(n,m)
	print(a,c)
	print(a-z,m-c,b+r)
	return 2*(b)*(b-1) == (b+r)*(b+r-1)

def checkR(r):
	b = 1
	n = 2*(b**2) + (r - b)
	m = (r+b) ** 2
	while(n < m):
		b *= 2
		n = 2*(b**2) + (r-b)
		m = (r+b) ** 2
	mn = 0	
	mx = b + 1
	while(mn < mx-1):
		md = (mx+mn)//2

		n = 2*(md**2) + r - md
		m = (r+md) ** 2
		if(n < m):
			mn = md
		elif(n > m):
			mx = md
		elif(n == m):
			return md
	return 0


s2 = 10**12//(2+math.sqrt(2)) - 10000
f = 0
t = 2
while(True):
	s2 += 1
	j = checkR(s2)
	if(j != 0):
		print(works(j,s2))
		print(j,s2,j + s2)
		print(int(j))
		f += 1
		if(f >= t):
			break
