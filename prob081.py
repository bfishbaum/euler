#Solved
m = open('p081_matrix.txt').read()
matrix = [[int(a) for a in line.split(',')] for line in m.splitlines()]

for row in range(len(matrix):
	for col in range(len(matrix[row])):
		if(row == 0 and col != 0):
			matrix[row][col] += matrix[row][col-1]
		elif(row == 0 and col != 0):
			matrix[row][col] += matrix[row-1][col]
		elif(row != 0 and col != 0):
			matrix[row][col] += min(matrix[row-1][col],matrix[row][col-1])
	
print(matrix[-1][-1])
				
			
