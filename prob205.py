#Solved
import random

# creates dictionary with all values and
# how many times they will appear out of all rolls
def createList(dice,sides):
	rollDict = {}
	def recurse(a,b,sum1):
		if(a == 0):
			rollDict[sum1] = rollDict.get(sum1,0) + 1
			return
		else:
			for x in range(1,b+1):
				recurse(a-1,b,sum1+x)
		return

	recurse(dice,sides,0)
	return rollDict

cDict = createList(6,6)
pDict = createList(9,4)

def countWins(dict1,dict2):
	keys1 = dict1.keys()
	keys2 = dict2.keys()
	wins1,ties,wins2 = 0,0,0
	
	for key1 in keys1:
		for key2 in keys2:
			occ = dict1[key1] * dict2[key2] 
			if(key1 > key2):
				wins1 += occ
			elif(key2 > key1):
				wins2 += occ
			else:
				ties += occ

	return wins1,ties,wins2

w,t,l = countWins(pDict,cDict)
winsPerc = w/(w+t+l)
print(winsPerc)
