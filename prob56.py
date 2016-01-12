#Solved
def digitSum(x):
	sum = 0
	while(x != 0):
		sum += x%10
		x //= 10
	return sum
maxSum = 0
for x in range(10**4):
	a = x % 100
	b = x//100 % 100
	dSum = digitSum(a**b)
	if(dSum > maxSum):
		maxSum = dSum
		print(a,b,dSum)
print(maxSum)
