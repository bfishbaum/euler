#Solved
import time
def isPermutation(x,y):
	x,y = str(x),str(y)
	for c in x:
		if(x.count(c) != y.count(c)):
			return False
	return True

def multiplesTo6(x):
	for i in range(2,6):
		if not isPermutation(x*i,x):
			return False
	return True
	
i = 0
while(True):
	i += 1
	if(multiplesTo6(i)):
		print(i)
		break
	
