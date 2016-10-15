#Solved
import time
scoreDict = {
		'HC':0,
		'1P':1,
		'2P':2,
		'3K':3,
		'ST':4,
		'FL':5,
		'FH':6,
		'4K':7,
		'SF':8,
		'RF':9
	}



def toInt(a):
	c1 = a[0]
	if(c1 == 'T'): c1 = 9
	elif(c1 == 'J'): c1 = 10
	elif(c1 == 'Q'): c1 = 11
	elif(c1 == 'K'): c1 = 12
	elif(c1 == 'A'): c1 = 0
	else: c1 = int(c1)-1

	c2 = a[1]
	if(c2 == 'C'): c2 = 0
	elif(c2 == 'D'): c2 = 1
	elif(c2 == 'H'): c2 = 2
	elif(c2 == 'S'): c2 = 3

	c = c2 * 13 + c1
	return c

def pairs(L):
	aL = sorted([l % 13 for l in L])
	counts = []
	for a in range(13):
		c = aL.count(a)
		if(c != 0):
			counts.append((a,c))
	t = sorted([a[1] for a in counts])	
	if(t == [1,4]):
		return '4K'
	elif(t == [2,3]):
		return 'FH'
	elif(t == [1,1,3]):
		return '3K'
	elif(t == [1,2,2]):
		return '2P'
	elif(t == [1,1,1,2]):
		return '1P'
	else:
		return 'HC'

def straight(L):
	aL = sorted([l % 13 for l in L])
	k = aL[0]
	aL = [l-k for l in aL]
	h = (aL == [0,1,2,3,4] or aL == [0,9,10,11,12])
	return h

def flush(L):
	a = L[0] // 13
	for b in L[1:]:
		if(b//13 != a):
			return False
	return True

def hand(L):
	l = [toInt(a) for a in L]
	s = straight(l)
	f = flush(l)
	k = [a % 13 for a in l]
	if(f and s):
		if(k == [0,9,10,11,12]):
			return 'RF'
		return 'SF'
	elif(f):
		return 'FL'
	elif(s):
		return 'ST'
	else:
		return pairs(l)
		 
hands = open('p054_poker.txt').read().splitlines()
p1 = [l.split(' ')[:5] for l in hands]
p2 = [l.split(' ')[5:] for l in hands]

def winner(a,b,scores):
	s1 = scores[a]
	s2 = scores[b]
	if(s1 > s2):
		return 1
	elif(s2 > s1):
		return 2
	else:
		assert(a == b)
		return 0

def breakTie(p1,p2,h1,h2):
	assert(h1 == h2)
	v1 = [toInt(a)%13 for a in p1]
	v2 = [toInt(a)%13 for a in p2]
	if(h1 not in ['SF','FL','ST','RF']):
		counts1 = []
		counts2 = []
		for a in range(13):
			c1 = v1.count(a)
			c2 = v2.count(a)
			if(c1 != 0):
				k = a
				if(k == 0):
					k = 13
				counts1.append((k,c1))
			if(c2 != 0):
				j = a
				if(j == 0):
					j = 13
				counts2.append((j,c2))

		counts1.sort(key = lambda(x):x[0],reverse = True)
		counts2.sort(key = lambda(x):x[0],reverse = True)
		counts1.sort(key = lambda(x):x[1],reverse = True)
		counts2.sort(key = lambda(x):x[1],reverse = True)

		for x in range(len(counts1)):
			if(counts1[x][0] > counts2[x][0]):
				return 1
			elif(counts1[x][0] < counts2[x][0]):
				return 2
		return 0
	else:
		if(0 in v1 and (12 in v1 or h1 == 'FL')):
			v1[v1.find(0)] == 13
		if(0 in v2 and (12 in v2 or h2 == 'FL')):
			v2[v2.find(0)] == 13
		v1.sort(reverse = True)
		v2.sort(reverse = True)
		for x in range(len(v1)):
			if(v1[x] > v2[x]):
				return 1
			elif(v1[x] < v2[x]):
				return 2
		return 0




t1 = 0
t2 = 0
for x in range(len(p1)):
	h1 = hand(p1[x])
	h2 = hand(p2[x])
	w = winner(h1,h2,scoreDict)
	if(w == 0):
		w = breakTie(p1[x],p2[x],h1,h2)	
	if(w == 1):
		t1 += 1
	if(w == 2):
		t2 += 1
	g = ['ST','FL','SF','RF','FH','4K']
	if(h2 in g or h1 in g):
		
		print(w)
		print(p1[x],h1)
		print(p2[x],h2)
print(t1)


