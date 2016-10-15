#Solved
import re
import sys
import math
sqrt = lambda x: math.ceil(math.sqrt(x))

w = re.sub(r'"','',open('p098_words.txt').read()).split(',')

def areAnagramicSquares(a,b,d):
	s = d[len(a)]
	L = []
	for i in s:
		letters = dict()
		for l in range(len(a)):
			letters[a[l]] = i[l]
		aN = ''.join([letters[c] for c in a])
		bN = ''.join([letters[c] for c in b])
		if(bN in s):
			L.append(int(bN))
			L.append(int(aN))
	if(L == []):
		return False
	return L

def hash_l(a):
	return hash(''.join(sorted(a)))


sqrs = [str(n**2) for n in range(1,100001) if len(set(str(n**2))) == len(str(n**2))]
sqrd = dict()
for k in sqrs:
	if(len(k) not in sqrd):
		sqrd[len(k)] = []	
	sqrd[len(k)] += [k]

sqrSet = set(sqrs)

d = dict()
for word in w:
	h = hash_l(word)
	d[h] = d.get(h,[]) + [word]

for x in d.keys():
	if(len(d[x]) <= 1):
		del(d[x])
	elif(not areAnagramicSquares(d[x][0],d[x][1],sqrd)):
		del(d[x])

pair = max(d.values(),key=lambda x:len(x[0]))
print(max(areAnagramicSquares(pair[0],pair[1],sqrd)))
	



