#Solved
import copy

m = open('p083_matrix.txt').read()
z = 80
matrix = [[[int(a),0] for a in line.split(',')[:z]] for line in
		m.splitlines()[:z]]
matrix[0][0][1] = matrix[0][0][0]

length = len(matrix)

def getSurBoxes(k,row,col):
	n = k[row][col]
	if(n[1] != 0):
		L = [n[1]]
	else:
		L = []
	if(col < len(k)-1):
		j = k[row][col+1][1]
		if(j > 0):
			L.append(k[row][col+1][1] + n[0])
	if(col > 0):
		j = k[row][col-1][1]
		if(j > 0):
			L.append(k[row][col-1][1] + n[0])
	if(row < len(k)-1):
		j = k[row+1][col][1]
		if(j > 0):
			L.append(k[row+1][col][1] + n[0])
	if(row > 0):
		j = k[row-1][col][1]
		if(j > 0):
			L.append(k[row-1][col][1] + n[0])
	if(L != []):
		x = min(L)
		n.append(x)
	else:
		x = n[-1]
		n.append(x)

def updateMatrix(L):
	length = len(L)
	for row in range(length):
		for col in range(length):
			getSurBoxes(L,row,col)
	for row in range(length):
		for col in range(length):
			L[row][col][1] = L[row][col].pop(2)

checker = []
while(checker != matrix):
	checker = copy.deepcopy(matrix)
	updateMatrix(matrix)

print(matrix[-1][-1])
