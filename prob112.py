#Solved
def inc(x):
	a = x%10
	x //= 10
	while(x != 0):
		if(x % 10 > a):
			return False
		else:
			a = x%10
		x //= 10
	return True

def dec(x):
	a = x%10
	x //= 10
	while(x != 0):
		if(x % 10 < a):
			return False
		else:
			a = x%10
		x //= 10
	return True

def bouncy(x):
	return not (inc(x) or dec(x))

counter = 0
i = 0
while(True):
	i += 1
	if(bouncy(i)):
		counter += 1	
	if(counter*100/i == 99):
		print(counter,i)
		break
	if(counter/i > 0.99):
		print(counter,i,"Notexact")
		break
