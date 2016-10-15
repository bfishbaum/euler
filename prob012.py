#Solved
def divisors(x):
	num = 0
	for i in range(1,int(x**0.5)+1):
		if(x%i == 0):
			num += 1

	num *= 2
	if(int(x**0.5)**2 == x):
		num -= 1
	return num

done = False
i = 0
t = 1
while(not done):
	i += 1
	t = (i+1)*i//2
	if divisors(t)>=500:
		done = True
print(t)
