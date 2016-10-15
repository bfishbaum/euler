import os
import re

def makeNewName(i):
	j = re.findall(r'[0-9]+',i)
	if(len(j) != 0):
		j = int(j[0])
		num = "%03d" % j
		new_name = 'prob' + num + '.py';
		print('prob' + num + '.py')
		return new_name
	return None

def is_euler_program(file_name):
	name_type1 = re.compile(r'prob[0-9]+.py')
	name_type2 = re.compile(r'pe[0-9]+.py')
	if(name_type1.match(file_name)):
		return True
	if(name_type2.match(file_name)):
		return True

regex = r".*\.py"
regex2 = r"prob.*"
l = []
for i in os.listdir("."):
	if(is_euler_program(i)):
		new_name = makeNewName(i)
		os.rename(i,new_name);
		

