#Solved
import permutations
def legitSet(a,b):
	for x in range(1,10):
		string1 = "0" + str(x**2)
		c1 = int(string1[-1])
		c2 = int(string1[-2])
		if (c1 not in a or c2 not in b) and (c1 not in b or c2 not in a):
			return False
	return True

def allSets():
	digits = list(range(10))
	allSet = [set(x) for x in permutations.chooseN(digits,6)]
	for set1 in allSet:
		if(6 in set1):
			set1.add(9)
		elif(9 in set1):
			set1.add(6)
	return permutations.chooseN(allSet,2)


	
total = 0
a = allSets()
for x in allSets():
	if(legitSet(x[0],x[1])):
		total += 1
print(total)
			
