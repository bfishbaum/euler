def isDone(t,tL):
	if(t not in tL):
		tL.append(t)
		return 0
	else:
		x = tL.index(t)
		return len(tL)-x

def divOne(b):
	s = '.'
	t = 10
	tL = [10]
	while(t != 0):
		if(b > t):
			s += '0'
			t *= 10
			i = isDone(t,tL)
			if(i != 0): return i
		else:
			h = t//b
			t -= h*b
			t *= 10
			s += str(h)
			i = isDone(t,tL)
			if(i != 0): return i
	return 0

print max([(x,divOne(x)) for x in range(1,1000)],key=lambda x:x[1])[0]
