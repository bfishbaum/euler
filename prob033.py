#Solved
def reduceFraction(x):
	gcd1 = gcd(x[0],x[1])
	return (x[0]//gcd1,x[1]//gcd1)

def product(a):
	numerator = 1
	denominator = 1
	for x in a:
		numerator *= x[0]
		denominator *= x[1]
	return (numerator, denominator)

def gcd(x,y):
	return gcd(y,x%y) if y != 0 else x


result = []
for x in range(10,100):
	for y in range(x+1,100):
		frac = (x,y)
		if(x % 10 != 0 and y % 10 != 0):
			if(x%10 == y//10):
				newFrac = (x//10,y%10)
				if(reduceFraction(frac) == reduceFraction(newFrac)):
					result.append(frac)
			elif(x//10 == y%10):
				newFrac = (x%10,y//10)
				if(reduceFraction(frac) == reduceFraction(newFrac)):
					result.append(frac)
print(result)
print(product(result))
print(reduceFraction(product(result)))
