#Solved
import prime

def getNextTwo(row,index,tri):
	try:
		return (tri[row+1][index],tri[row+1][index+1])	
	except:
		return None

def getAboveTwo(row,index,tri):
	result = []
	try:
		if(index != 0):
			result.append(tri[row-1][index-1])
		result.append(tri[row-1][index])
	except: pass
	return result

def maxPath():
	file = prime.readFile("resources/67.txt")
	file = file.splitlines() 
	tri = [[int(y) for y in x.split(" ")] for x in file]

	result = [tri[0]]
	for x in range(1,len(tri)):
		result.append([])
		for y in range(len(tri[x])):
			z = max(getAboveTwo(x,y,result))
			result[-1].append(tri[x][y] + z)
	return result

sums = maxPath()
print(sums[-1])
print(max(sums[-1]))
	
