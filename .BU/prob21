#Solved
def getSumDivisors(n):
	if(n <= 3):
		return 1
	divisors = []
	for x in range(1,int(n**0.5)+1):
		if(n%x == 0):
			divisors += [x]
		if(x*x == n):
			divisors = divisors[0:-1]
	sum = 0
	for div in divisors:
		sum += div
		sum += n/div
	return (sum - n)
		

def amicableNo(x):
	y = getSumDivisors(x)
	z = getSumDivisors(y)
	if(x == z and x != y):
		return y
	return None

sum = 0
for x in range(3,10000):
	ami = amicableNo(x)
	if(ami != None):
		sum += x+ami
print(sum/2)

