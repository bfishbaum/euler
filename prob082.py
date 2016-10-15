#Solved
m = open('p082_matrix.txt').read()
matrix = [[[int(a),int(a)] for a in line.split(',')] for line in m.splitlines()]
length = len(matrix)
for col in range(1,length):
	for row in range(length):
		k = matrix[row][col]
		k[1] = matrix[row][col-1][1] + k[0]
	if(col < length-1):
		# this line is important to ensure
		# that if two vertical movements are 
		# made in the same column
		for x in range(length):
			for row in range(length):
				k = matrix[row][col]
				a = [k[1]]
				if(row >= 1):
					a.append(matrix[row-1][col][1] + k[0])
				if(row < length-1):
					a.append(matrix[row+1][col][1] + k[0])
				k.append(min(a))

			for row in range(length):
				k = matrix[row][col]
				k[1] = k.pop(2)

print(min([k[-1][1] for k in matrix]))
