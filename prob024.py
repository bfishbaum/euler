def fac(x):
	t = 1
	while(x > 1):
		t *= x
		x -= 1
	return t

t = 10
n = [z for z in range(t)]
l = ''
m = 10**6
m = m-1
for x in range(t-1,-1,-1):
	f = fac(x)
	i = m//f
	m -= i*f
	l += str(n.pop(i)) + ' '
	print(l)
	
