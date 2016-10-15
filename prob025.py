#Solved
import math
def nthFib(n):
	n = n-1
	if(n <= 1):
		return 1
	x = 1
	y = 1
	for a in range(n-1):
		z = x+y
		x = y
		y = z
	return y

x = 1
y = 1
n = 2
while(math.log(y,10) < 999):
	n += 1
	z = x+y
	x = y
	y = z
print(n,y)
