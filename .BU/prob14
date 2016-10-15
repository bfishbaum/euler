#Solved
def collatzStep(x):
	if(x % 2 == 0):
		return x//2
	else:
		return x*3+1


def collatzLength(n):
	values = {1:0}
	valueSet = set([1])
	def collatzRecurse(x):
		if(x in valueSet):
			return values[x]
		else:
			y = collatzRecurse(collatzStep(x))
			valueSet.add(x)
			values[x] = y+1
			return y+1

	maxLength = (0,1)
	for i in range(1,n):
		z = collatzRecurse(i)
		if(z > maxLength[0]):
			maxLength = (z,i)

	return maxLength

def collatzString(n):
	if(n == 1):
		return [1]
	else:
		return [n] + collatzString(collatzStep(n))

x = collatzLength(1000000)
print(x[1])
