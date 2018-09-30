from stopwords import stopwords_list
import re
from collections import Counter
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
temp = []

def makenorm(word):
	word = morph.parse(word)[0]
	return word.normal_form

with open('News.txt', 'r', encoding='utf-8-sig') as source:
	for line in source:
		temp.extend(re.split('[^a-zA-Zа-яА-Я|ё|Ё]', line.lower(), maxsplit = 0))

temp = [elem for elem in temp if elem and not elem in stopwords_list
        and elem != 'автор' and elem != 'дата' and not re.fullmatch('\w', elem)]
temp = list(map(makenorm, temp))

popularity = Counter(temp)
popularity = popularity.most_common(30)

with open('PopularWords.txt', 'w') as result:
	for elem in popularity:
		print(elem)
		result.write(str(elem) + '\n')
