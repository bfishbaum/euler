p = '''\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
pyr = []
for l in p.splitlines():
	x = [[int(a),0] for a in l.split(' ')]
	pyr.append(x)

pyr[0][0][1] = pyr[0][0][0]
for s in range(1,len(pyr)):
	stage = pyr[s]
	for i in range(len(stage)):
		b = stage[i]
		if(i == 0):
			b[1] = pyr[s-1][0][1] + b[0]
		elif(i == len(stage)-1):
			b[1] = pyr[s-1][i-1][1] + b[0]
		else:
			b[1] = max(pyr[s-1][i-1][1],pyr[s-1][i][1]) + b[0]

print(max(pyr[-1],key=lambda x: x[1]))


