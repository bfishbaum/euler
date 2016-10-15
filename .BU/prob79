#Solved

x = "319680180690129620762689762318368710720710629168160689716731736729316729729710769290719680318389162289162718729319790680890362319760316729380319728716"
attempts = [x[3*i:3*i+3] for i in range(50)]

def attemptInCode(attempt,code):
	index = 0
	for x in attempt:
		if(x in code[index:]):
			index += code[index:].index(x)
		else:
			return False
	return True

def allAttemptsInCode(attempts,code):
	for attempt in attempts:
		if(not attemptInCode(attempt,code)):
			return False
	return True

def allDoubles(attempts):
	allPairs = []
	for attempt in attempts:
		for x in range(len(attempt)-1):
			allPairs += [(attempt[x],attempt[x+1])]
	allPairs = removeMultiples(allPairs)
	return(allPairs)


def removeMultiples(n):
	x = sorted(n)
	i = 0
	while i < len(x)-1:
		if(x[i] == x[i+1]):
			x.pop(i+1)
		else:
			i += 1
	return x

def addAttemptToCode(attempt,code):
	pass	

def subtractive(attempts,code):
	i = 0
	while i < len(code):
		if(allAttemptsInCode(attempts,code[:i]+code[i+1:])):
			code = code[:i]+code[i+1:]
		else:
			i += 1
	return code

def additive(attempts):
	allPairs = allDoubles(attempts)
	code = allPairs[0]
	i = 0
	while i < len(allPairs):
		print(allPairs[i],code)
		if(areDisjoint(allPairs[i],code)):
			allPairs.append(allPairs.pop(i))
			print(i)
		elif(not attemptInCode(allPairs[i],code)):
			a = allPairs[i][0]
			b = allPairs[i][1]

			switch = True
			try: findA = code.index(a)
			except:
				switch = False
				code = tuple(a) + code

			try: findB = code.index(b)
			except:
				switch = False
				code += tuple(b)

			if(switch):
				code = code[:findB] + tuple(a) + code[findB+1:findA] + tuple(b) + code[findA+1:]
			i += 1
		else:
			i += 1
	return code


def areDisjoint(a,b):
	for x in a:
		if(x in b): return False
	return True

x = additive(attempts)
print(''.join(x))
