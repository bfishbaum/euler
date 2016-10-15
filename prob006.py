#Solved
def differenceOfSumsOfSquares(x):
	n1 = 0
	n2 = 0
	for i in range(x+1):
		n1 += i**2
		n2 += i
	n2 = n2**2
	print(n2-n1)
print(differenceOfSumsOfSquares(100))
