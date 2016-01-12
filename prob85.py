#Solved
import permutations as pr
i = 3
done = False
best = 2000000
while(pr.nCr(i,2) < 2 * 10 ** 6):
	i += 1
	for x in range(1,i+1):
		z = pr.nCr(i+1,2) * pr.nCr(x+1,2)
		if(abs(z - 2000000) < best):
			print(i,x,i*x,z)
			best = abs(z-2000000)

