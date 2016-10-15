#Solved
def contFrac(values):
	temp = values.pop()
	while len(values) > 0:
		temp = values.pop() + 1/temp
	return temp

def contFraction(values):
	frac = (values.pop(),1)

	def addToFrac(fract,add):
		return (fract[0]+add*fract[1],fract[1])
	
	while(values != []):
		frac = addToFrac(frac[::-1],values.pop())
	
	return frac

def eValue(length):
	result = [2]
	for x in range(1,length//3+2):
		result.append(1) 
		result.append(2*x) 
		result.append(1) 
	return result[:length]

def digitSum(x):
	sum = 0
	while(x != 0):
		sum += x%10
		x //= 10
	return sum

print(digitSum(contFraction(eValue(100))[0]))
#6472192446
