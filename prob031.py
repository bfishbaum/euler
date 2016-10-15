#Solved
# one will be added for 200 coin
coins = [1,2,5,10,20,50,100,200]
def partitions(x,i):
	aD = {}
	def rec(x,i):
		if((x,i) in aD): return aD[(x,i)]
		tot = 0
		if(x == 0):
			aD[(x,i)] = 1
			return 1	
		if(i < 0):
			aD[(x,i)] = 0
			return 0
		for k in range(0,x//coins[i]+1):
			a = rec(x-coins[i]*k,i-1)
			tot += rec(x-coins[i]*k,i-1)
		aD[(x,i)] = tot
		return tot
	return rec(x,i)

print(partitions(200,len(coins)-1))
