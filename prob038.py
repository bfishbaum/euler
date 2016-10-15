#Solved
def isPanX(n):
	m = ''
	c = 1
	while(len(m) < 9):
		m += str(c * n)
		c += 1
	return m,isPandig(m)
		
	
def isPandig(z):
	return ''.join(sorted(z)) == '123456789'

m = []
for x in range(9876):
	a,b = isPanX(x)
	if(b):
		m += [(x,int(a))]

print(max(m,key=lambda x:x[1]))
