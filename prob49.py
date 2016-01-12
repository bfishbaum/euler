#Solved
import prime as pi
import permutations as pr
sieve = [x for x in pi.sieve(10000) if x > 1000]
dict1 = {}
def hash1(x):
	return ''.join(sorted(str(x)))


for x in sieve:
	h = hash1(x)
	dict1[h] = dict1.get(h,[]) + [x]

keys = dict1.keys()
triplets = []
for key in keys:
	x = dict1[key]
	if(len(x) >= 3):
		triplets.append(x)

for y in triplets:
	for x in pr.chooseN(y,3):
		x.sort()
		if(x[2] - x[1] == x[1] - x[0]):
			x = [str(a) for a in x]
			print(''.join(x),"Done")
			break
	
