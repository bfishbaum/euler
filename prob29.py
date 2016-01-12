#Solved
set1 = set()
for x in range(2,101):
	for y in range(2,101):
		set1.add(x**y)

print(len(list(set1)))
