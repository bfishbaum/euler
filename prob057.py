#Solved
def gcd(x,y):
	while(x != 0):
		x,y = y%x,x
	return y

def red(n,d):
	g = gcd(n,d)
	return n//g,d//g

def div(a,b):
	if(b[0] == 0):
		raise ZeroDivisionError
	n = a[0]*b[1]
	d = a[1]*b[0]
	return red(n,d)

def mul(a,b):
	n = a[0]*b[0]
	d = a[1]*b[1]
	return red(n,d)

def add(a,b):
	n = a[0]*b[1] + a[1]*b[0]
	d = a[1]*b[1]
	return red(n,d)

def sub(a,b):
	n = a[0]*b[1] - a[1]*b[0]
	d = a[1]*b[1]
	return red(n,d)

def approx(a,(b,c)=((1,1),0)):
	t = b
	for x in range(a-c):
		k = add(t,(1,1))
		n = div((1,1),k)
		t = add((1,1),n)
	return t

b = (1,1)
c = (0)
total = 0
for x in range(1,1001):
	b = approx(x,(b,x-1))
	if(len(str(b[0])) > len(str(b[1]))):
		total += 1
print(total)
