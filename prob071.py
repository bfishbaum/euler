#Solved
import fraction
min = (0,1)
for x in range(1,1000000):
	for y in range(max(1,3*x//7 - 1),3*x//7 + 1):
		if(y/x >= 3/7): break		
		elif (y/x > min[0]/min[1]):
			min = (y,x)

print(min)
