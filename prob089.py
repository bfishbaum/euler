#Solved
import prime

def romToNum(roman):
	romDict = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
	roman = roman.lower()
	sum = 0
	for x in range(len(roman)-1):
		if(romDict[roman[x]] < romDict[roman[x+1]]):
			sum -= romDict[roman[x]]
		else:
			sum += romDict[roman[x]]
	sum += romDict[roman[-1]]
	return sum

def minimal(num):
	fin = ""
	fin += "M" * (num//1000)
	num %= 1000
	if(num >= 900):
		fin += "CM"
		num %= 900
	elif(num >= 500):
		fin += "D"
		num %= 500
	elif(num >= 400):
		fin += "CD"
		num %= 400
	fin += "C" * (num//100)
	num %= 100
	if(num >= 90):
		fin += "XC"
		num %= 90
	elif(num >= 50):
		fin += "L"
		num %= 50
	elif(num >= 40):
		fin += "XL"
		num %= 40
	fin += "X" * (num//10)
	num %= 10
	if(num == 9):
		fin += "IX"
		num %= 9
	elif(num >= 5):
		fin += "V"
		num %= 5
	elif(num >= 4):
		fin += "IV"
		num %= 4
	fin += "I" * num
	return fin

roms = prime.readFile("resources/89.txt").splitlines()
total = 0
for rom in roms:
	newRom = minimal(romToNum(rom))
	total += len(rom) - len(newRom)
print(total)
