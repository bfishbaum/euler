#Solved
import time
def check(x):
	str1 = "987654321"
	a = x % 10
	counter = 0
	while(x > 0):
		if(a != int(str1[counter])): return False
		x //= 100
		a = x % 10
		counter += 1
	return True

def check2(x):
	str1 = "123456789"
	return str(x)[::2] == str1
	
def mergeStrings(x,y):
	a = min(len(x),len(y))
	new = ""
	for b in range(a):
		new += x[b] + y[b]
	return new + x[a:] + y[a:]
tim = time.time()
for x in range(100000000,150000000,10):
	i1 = x + 3
	i2 = x + 7
	if(check2(i1**2)):
		print(i1,i1**2)
		break
	if(check2(i2**2)):
		print(i2,i2**2)
		break
tim2 = time.time()
print(tim2-tim)
