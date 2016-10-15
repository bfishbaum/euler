#Solved
x = [0,1]
while(x[-1] < 4000000):
	x.append(x[-1]+x[-2])
x = x[:-1]
print(x)
sum = 0
for y in x:
	if(y % 2 == 0):
		sum += y
print(sum)
