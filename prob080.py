#Solved
import math

def sqrt(n,accuracy = 5):
	accuracy = max(int(math.log(n,2)),accuracy)
	guess = int(n+1)//2
	for i in range(accuracy): guess = int((guess + n//guess)//2)
	if(int(guess)**2 == n): return int(guess)
	elif (int(guess) + 1)**2 == n: return int(guess) + 1
	else: return guess

def sumFirst100(x):
	x = str(x)[:100]
	total = 0
	for c in x:
		total += int(c)
	return total

total = 0
for x in range(1,101):
	square = sqrt(x*10**500,10000)
	print(square)
	print(math.log(square,10))
	if(str(square).count("0") < 100):
		total += sumFirst100(square)
	print(x)
print(total)
