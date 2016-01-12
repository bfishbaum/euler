#Solved
def isPyTrip(a,b,c):
	return (a**2+b**2==c**2)
	
def createPyTrip(x):
	if(x % 2 == 0):
		b = x**2//4 - 1
		c = x**2//4 + 1
	else:
		b = x**2//2
		c = x**2//2+1
	return (x,b,c)
i = 3
while(True):
	py3 = createPyTrip(i)
	pysum = sum(py3)
	if(1000 % pysum == 0):
		mult = 1000//pysum
		print(py3[0],py3[1],py3[2])
		print(py3[0]*py3[1]*py3[2]*mult**3)
		break
	i += 1
