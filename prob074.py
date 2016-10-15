#Solved
def factorial(x):
	product = 1
	while(x > 1):
		product *= x
		x -= 1
	return product

facts = [factorial(x) for x in range(10)]
def digitFact(x):
	sum = 0
	while(x != 0):
		sum += facts[x%10]
		x //= 10
	return sum

def chainLength(x):
	total = 1
	previous = set()
	previous.add(x)
	while(True):
		x = digitFact(x)
		if(x in previous):
			return total
		else:
			previous.add(x)
			total += 1

total = 0
for x in range(1000000):
	if(chainLength(x) == 60):
		total += 1
	if(x % 1000 == 0):
		print(x)

print(total)
	
