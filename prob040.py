#Solved
def p10Digs(x):
	#how many digits are between 10**x to 10**(x+1)-1
	return 9 * (x+1) * 10**x

def getNthDigit(k):
	x = k
	c = 0
	while(x > p10Digs(c)):
		x -= p10Digs(c)
		c += 1
	a = (x-1)//(c+1)
	x -= a*(c+1)
	r = 10**c + a
	return str(r)[x-1]
		
total = 1
for x in range(7):
	k = 10**x
	total *= int(getNthDigit(k))
print(total)
