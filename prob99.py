#Solved
import prime
import math
numbers = [(int(a.split(",")[0]),int(a.split(",")[1]))
			 for a in prime.readFile("resources/99.txt").splitlines()]

def compareExps(a,b):
	print(a,b,end=" ")
	aLogb = math.log(a[0],b[0])	
	print(aLogb)
	if(b[1] / aLogb > a[1]):
		return b
	else: return a

numbers2 = numbers[:]

while (len(numbers) > 1):
	a = numbers.pop(0)
	b = numbers.pop(0)
	numbers.append(compareExps(a,b))
print(numbers[0])
print(numbers2.index(numbers[0]))




