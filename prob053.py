#Solved
def nCr(n,r):
	r = max(r,n-r)
	product = 1
	for x in range(r+1,n+1):
		product *= x
	for y in range(1,n-r+1):
		product //= y
	return product

i = 0
for x in range(1,101):
	for y in range(1,x+1):
		if(nCr(x,y) > 1000000):
			print(x,y,nCr(x,y))
			i += 1
print(i)
	
