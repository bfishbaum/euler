#Solved
def sumOfDigitsToNth(x,n):
	if(x == 0):
		return 0
	else:
		return (x%10)**n + sumOfDigitsToNth(x//10,n)

sum = 0
for i in range(2,500000):
	if(sumOfDigitsToNth(i,5) == i):
		sum += i
print(sum)

