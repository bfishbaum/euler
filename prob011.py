#Solved
import prime as pi
matrix = pi.readFile("resources/11.txt")
matrix = [[int(x) for x in j.split(" ")] for j in matrix.splitlines()]
def product(x):
	product = 1
	for y in x:
		product *= y
	return product

def iterate2DList(x):
	max = 0
	for row in range(len(x)):
		for col in range(len(x[row])):
			z = searchDirAtPoint(row,col,x,max)
			if(z > max): max = z
	return max
			

def searchDirAtPoint(row,col,board,max):
	dirs = [(dRow,dCol) for dRow in range(-1,2) for dCol in range(-1,2)]
	dirs.pop(4)
	for dir in dirs:
		try:
			product = 1
			list1 = []
			for i in range(4):
				z = board[row + dir[0] * i][col + dir[1] * i]
				product *= z
				list1 += [z]
			if product > max:
				max = product
				print(product,row,col,dir,list1)
		except: pass
	return max

print(iterate2DList(matrix))
