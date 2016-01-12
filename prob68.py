#Solved
import permutations as pr
def getLine(n,pent):
	inner = pent[0]
	outer = pent[1]
	a = outer[n]
	b = inner[n]
	c = inner[(n+1)%5]
	return [a,b,c]

def legitPent(pent):
	x = sum(getLine(0,pent))
	for a in range(1,5):
		if(sum(getLine(a,pent)) != x):
			return False
	return True

def pentString(pent):
	inner = pent[0]
	outer = pent[1]
	ind = outer.index(min(outer))
	pentString = ""
	for x in range(ind,ind+5):
		y = x % 5
		pentString += ''.join([str(a) for a in getLine(y,pent)])
	return pentString

def createPents():
	a = [x for x in range(1,10)]
	perms = [list2Pent(b + [10]) for b in pr.permute(a) if legitPent(list2Pent(b + [10]))]
	return perms

def list2Pent(s):
	outer = [c for c in s[5:]]
	inner = [c for c in s[:5]]
	return [inner,outer]

pents = createPents()
print(max([int(pentString(pent)) for pent in pents]))
