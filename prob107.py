#Solved
import prime as pi
import copy
def print2DArray(x):
	for a in x:
		print("[",end = " ")
		for b in a:
			print("{:>3}".format(b),end ="|")
		print("]")

def connectedNetwork(network):
	connected = [a == 0 for a in range(len(network))]
	visited = set()
	# every time a node is reached
	# go to every unvisited node
	# set node to True when visited
	def recurse(index):
		if(index not in visited):
			visited.add(index)
			connected[index] = True
			node = network[index]
			for x in range(len(node)):
				if(x not in visited):
					if node[x]:
						recurse(x)

	# start at first node	
	recurse(1)
	# make sure all nodes have been visited
	return False not in connected

def sumLengths(network):
	sum = 0
	for x in network:
		for y in x:
			sum += y
	return sum//2

def maxConnect(network):
	maxP = (0,0)
	for x in range(len(network)):
		for y in range(x+1,len(network[x])):
			if(network[x][y] > network[maxP[0]][maxP[1]]):
				maxP = (x,y)
	return maxP

def isRemovable(x,y,network):
	temp = copy.deepcopy(network)
	removeConnection(x,y,temp)
	return connectedNetwork(temp)

def maxRedunConnect(network):
	max1 = 0
	maxP = None
	for x in range(len(network)):
		for y in range(x+1,len(network[x])):
			if(network[x][y] > max1):
				if(isRemovable(x,y,network)):
					maxP = (x,y)
	return maxP

def isMinimized(network):
	for x in range(len(network)):
		for y in range(x+1,len(network[x])):
			if(not network[x][y]):
				temp = copy.deepcopy(network)
				removeConnection(x,y,temp)
				if(connectedNetwork(temp)):
					return False
	return True

def removeConnection(row,col,network):
	network[row][col] = 0 
	network[col][row] = 0 

def sortNetwork(network):
	L = []
	for x in range(len(network)):
		for y in range(x+1,len(network[x])):
			z = (x,y,network[x][y])
			L.append(z)
	return [r for r in sorted(L,key = lambda x: x[2],reverse = True) if r[2]]
				
def createMatrix():
	netMatrixString = pi.readFile("resources/107.txt")
	temp = netMatrixString.splitlines()
	# special code, 0's represent no connection
	# otherwise the distance represents it
	netMatrix = [[int(a*(a != "-") + "0"*(a == "-")) for a in x.split(",")] for x in temp]
	return netMatrix

def minimizeNetwork(network):
	tuples = sortNetwork(network)
	network = copy.deepcopy(network)
	i = 0
	total = sumLengths(network)
	while(i < len(tuples)):
		pt = tuples[i][:2]
		size = tuples[i][2]
		if(isRemovable(pt[0],pt[1],network)):
			total -= size
			print(size)
			removeConnection(pt[0],pt[1],network)
		i += 1
	return network
	
network = createMatrix()
tot1 = sumLengths(network)
minimized = minimizeNetwork(network)
tot2 = sumLengths(minimized)

print(tot1,tot2,tot1-tot2)

