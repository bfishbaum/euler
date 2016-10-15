import re
x = open('p022_names.txt','r').read()
x = re.sub(re.compile('",'),'',x)
z = x.split('"')
z.sort()
z.pop(0)
z.pop(0)

total = 0
for x in range(1,len(z)+1):
	name = z[x-1]
	total += sum([ord(n)-64 for n in name]) * x
print(total)
	
