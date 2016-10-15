#Solved
import prime
def isAbundant(x):
	return x < sum(prime.getFactors(x))

allAbNos = []
for x in range(12,28125):
	if(isAbundant(x)):
		allAbNos += [x]

allAbNosSet = set(allAbNos)

sum1 = 0
for x in range(1,28125):
	noSum = True
	for no in allAbNos:
		if((x - no) in allAbNosSet):
			noSum = False
			break
	if noSum:
		sum1 += x
print(sum1)
