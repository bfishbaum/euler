#Solved
def polygonalNumber(ngon,index):
	if(ngon < 3): return 0
	else:
		a = index * (index + 1) // 2
		b = (ngon-3) * index * (index-1) // 2
		return a + b

def existsPoly(ngon,num):
	i = 0
	value = 0
	while(value < num):
		i += 1
		value = polygonalNumber(ngon,i)
		if(value == num):
			return True
	return False

pen = set([polygonalNumber(5,x) for x in range(10000)])
sex = set([polygonalNumber(6,x) for x in range(10000)])

i = 0
setNum = 10000
maxNum = polygonalNumber(5,setNum)
while True:
	i += 1
	tri = polygonalNumber(3,i)
	if(tri > maxNum):
		for x in range(setNum,setNum*2):
			pen.add(polygonalNumber(5,x))
			sex.add(polygonalNumber(6,x))
		setNum = setNum * 2
		maxNum = polygonalNumber(5,setNum)
	if(tri in pen and tri in sex):
		print(tri)
	
	
	
