#Solved
import math

sum = 0
for base in range(1,10):
	for exp in range(1,22):
		power = base**exp
		digits = math.floor(math.log(power,10)) + 1
		if(digits == exp):
			sum += 1
		else:
			break

print(sum)
	
	
