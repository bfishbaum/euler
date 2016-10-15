mD = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def addWeek(date):
	d = date[0]
	m = date[1]
	y = date[2]
	d += 7
	if(d > mD[m]):
		d -= mD[m]
		m += 1
	if(m > 12):
		y += 1
		print(y)
		if((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
			mD[2] = 29
		else:
			mD[2] = 28
		m = 1
	date[0] = d
	date[1] = m
	date[2] = y

total = 0
date = [7,1,1900]
while(date[2] < 2001):
	addWeek(date)
	if(date[0] == 1 and date[2] <= 2000 and date[2] > 1900):
		total += 1
print(total)
