with open('anaconda.txt', 'r') as source:
	with open('result.txt', 'w') as result:
		for line in source:
			line = line.lower()
			line = line.replace('snake','python')
			if 'python' in line and 'anaconda' in line:
				print(line)
				result.write(line)