#Solved
import prime as pi
import fraction as fr
import math

total = 0
for x in range(2,12001):
	for y in range(x//3+1,math.ceil(x/2)):
		if(fr.gcd(x,y) == 1):
			total += 1

print(total)
