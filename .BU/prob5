#Solved
import prime

def smallestMultiple(x):
	allFactors = []
	for i in range(2,x):
		factors = prime.primeFactors(i)
		factorSet = list(set(allFactors+factors))
		newSet = []
		for factor in factorSet:
			newSet += [factor] * max(factors.count(factor),allFactors.count(factor))
		allFactors = newSet
	return allFactors

def product(x):
	product = 1
	for y in x:
		product *= y
	return product

for i in range(21):
	print(product(smallestMultiple(i)))
