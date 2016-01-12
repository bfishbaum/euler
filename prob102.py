#Solved
import prime
def createLine(p1,p2):
	if(p1[0] == p2[0]):
		return ("inf",p1[0])
		print("DW")
	else:
		m = (p1[1]-p2[1])/(p1[0]-p2[0])
		b = (p1[1]-m*p1[0])
		return (m,b)

def pointLine(point,line):
	if(line[0] == "inf"):
		if(line[1] == point[0]):
			return 0
		elif(line[1] > point[0]):
			return -1
		else:
			return 1
	else:
		y1 = point[1]
		y2 = line[0]*point[0] + line[1]
		if(y1 == y2):
			return 0
		elif(y2 > y1):
			return -1
		else:
			return 1

def triContainsOrigin(tri):
	p1,p2,p3,o = tri[0],tri[1],tri[2],(0,0)	
	s1 = createLine(p2,p3)
	s2 = createLine(p1,p3)
	s3 = createLine(p1,p2)
	if(pointLine(p1,s1) != pointLine(o,s1)):
		return False
	if(pointLine(p2,s2) != pointLine(o,s2)):
		return False
	if(pointLine(p3,s3) != pointLine(o,s3)):
		return False
	return True

triangles = prime.readFile("resources/102.txt").splitlines()
tris = []
for tri in triangles:
	a = [int(x) for x in tri.split(",")]
	s1 = (a[0],a[1])
	s2 = (a[2],a[3])
	s3 = (a[4],a[5])
	tris.append((s1,s2,s3))

total = 0
for x in tris:
	if(triContainsOrigin(x)):
		total += 1
print(total)
	
