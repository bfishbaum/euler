#Solved
import math
def qf(a,b,c):
	k = (b**2-4*a*c)
	if(k < 0):
		return 0
	q = math.sqrt(k)
	return (-b + q)/(2*a)

def isTriN(x):
	if(x == 0): return False
	q = int(qf(1,1,-2*x))
	return q**2+q == 2*x

for x in range(100):
	if(isTriN(x)):
		print(x)

def word(x):
	t = 0
	for c in x:
		t += ord(c) - 96
	return t

words = open('p042_words.txt','r').read().split('","')
words[0] = words[0][1:]
words[-1] = words[-1][:-1]
t = 0
for w in words:
	score = word(w.lower())
	if(isTriN(score)):
		print(score,w)
		t += 1
print t
