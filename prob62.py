#Solved
import permutations as pr
import math
def hashNum(x):
	return ''.join(sorted(list(str(x))))	


cubeDict = {}
i = 0
leng = 1
while(True):
	i += 1
	cube = i**3
	leng1 = int(math.log(cube,10)) + 1
	if(leng1 != leng):
		cubeDict = {}
		leng = leng1
	hashC = hashNum(cube)
	if(cubeDict.get(hashC,0) == 0):
		cubeDict[hashC] = [cube]
	else:
		cubeDict[hashC] += [cube]
	lst = cubeDict[hashC]
	if(len(lst) == 5):
		print(min(lst))
		break
	
