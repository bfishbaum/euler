#Solved
def revAdd(a):
	return a + int(str(a)[::-1])

def isP(a):
	return str(a) == str(a)[::-1]

def isLychrel(a,s):
	for x in range(50):
		a = revAdd(a)
		if(isP(a)):
			return False
		if(a in s):
			return True
	return True

LS = set()
total = 0
for x in range(9999,0,-1):
	if(isLychrel(x,LS)):
		total += 1
		LS.add(x)
print(total)


