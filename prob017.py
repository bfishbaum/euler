bigDict = {
0:'',
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine',
10:'ten',
11:'eleven',
12:'twelve',
13:'thirteen',
14:'fourteen',
15:'fifteen',
16:'sixteen',
17:'seventeen',
18:'eighteen',
19:'nineteen',
20:'twenty',
30:'thirty',
40:'forty',
50:'fifty',
60:'sixty',
70:'seventy',
80:'eighty',
90:'ninety',
100:'hundred'}

def letterCount(x):
	x = abs(x)
	s = str(x)
	total = 0
	if(len(s) >= 4):
		if(x == 1000):
			return 11
	if(len(s) == 3):
		total += len(bigDict[int(s[0])] + bigDict[100] + 'and')
		x = x % 100
		s = str(x)
		if(x == 0):
			return total - 3
	if(len(s) == 2):
		if(x < 20):
			total += len(bigDict[x])
			return total
		else:
			total += len(bigDict[x-x%10])
			x = x % 10
			s = str(x)
	if(len(s) == 1):
		total += len(bigDict[x])
	return total
print(sum([letterCount(z) for z in range(1,1001)]))
