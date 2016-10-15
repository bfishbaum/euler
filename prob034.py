#Solved
def factorial(x):
	product = 1
	for y in range(2,x+1):
		product *= y
	return product
		
def factDigits(x):
	sum = 0
	while(x != 0):
		sum += factorial(x%10)
		x //= 10
	return sum

sum = 0
for i in range(3,200000):
	if(factDigits(i) == i):
		sum += i
		print(i)
print(sum)
	
