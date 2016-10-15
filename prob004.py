#Solved
def largestPalindromeProduct():
	list1 = []
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			x = str(i*j)
			if(x == x[::-1]):
				list1.append(i*j)
	return sorted(list1)

print(largestPalindromeProduct())
