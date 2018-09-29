import re

temp = []
tempy = []
years = set()
words = set()

with open('anaconda.txt', 'r') as source:
	for line in source:
		temp.extend(re.split('[^a-zA-Z]', line, maxsplit = 0))
		tempy.extend(re.split('\D+', line, maxsplit = 0))
	words = set(elem for elem in temp if elem)
	years = sorted(set(elem for elem in tempy
                           if re.fullmatch('\d\d\d\d', elem)))
	

print(years)

with open('words.txt', 'w') as result:
	for elem in words: 
		result.write(str(elem) + '\n')
with open('years.txt', 'w') as result2:
	for elem in years: 
		result2.write(str(elem) + '\n')
