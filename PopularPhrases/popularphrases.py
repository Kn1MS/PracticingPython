from stopwords import stopwords_list
import re
from collections import Counter
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
temp = []
wordslist = []
popwordslist = []
phrases = []

def makenorm(word):
	word = morph.parse(word)[0]
	return word.normal_form

print ('Creating words list...\n')
with open('News.txt', 'r', encoding='utf-8-sig') as source:
	for line in source:
		wordslist.extend(re.split('[^a-zA-Zа-яА-Я|ё|Ё]', line.lower(), maxsplit = 0))

print ('Removing all the litter...\n')
wordslist = [elem for elem in wordslist if elem and not elem in stopwords_list 
			and elem != 'автор' and elem != 'дата' and not re.fullmatch('\w', elem)]
wordslist = list(map(makenorm, wordslist))

print ('Creating counter for list...\n')
popularity = Counter(wordslist)
popularity = popularity.most_common(5)

#У нас есть список из 5 слов в каунтере. Стартом и эндом выдираем сами слова без всего лишнего, заносим в отдельный лист.
#Снова открываем основной файл. С помощью pymorphy чекаем каждое слово на то, не совпадает ли оно в нормальной форме с одним из наших.
#Если совпадает, то докидываем его в список популярных слов. После этого проходим по всему тексту, высматривая регуляркой словосочетания.
#Перезаписываем popularity под новый лист, т.е. делаем каунтер для словосочетаний.
#Выводим весь список и закидываем в файл, конец.

print ('Creating words list (without normal forms)...\n')
with open('News.txt', 'r', encoding='utf-8-sig') as source:
	for line in source:
		wordslist.extend(re.split('[^a-zA-Zа-яА-Я|ё|Ё]', line.lower(), maxsplit = 0))

print ('Removing all the litter...\n')
wordslist = [elem for elem in wordslist if elem and not elem in stopwords_list 
			and elem != 'автор' and elem != 'дата' and not re.fullmatch('\w', elem)]

print ('Creating popular words list...\n')
for elem in popularity:
	match = re.search('\w+', str(elem))
	popwordslist.append(str(elem)[match.start():match.end()])

print ('Checking normal forms and adding the matching ones...\n')
for elem in wordslist:
	for popword in popwordslist:
		if makenorm(elem) == popword and elem != popword:
			temp.append(elem)
popwordslist.extend(temp)
popwordslist = list(set(popwordslist))

print ('Creating phrases...\n')
with open('News.txt', 'r', encoding='utf-8-sig') as source:
	for line in source:
		for popword in popwordslist:
			match = re.search(f' {popword} \w+', line)
			if match:
				phrases.append(str(line)[match.start()+1:match.end()])

print ('DONE! Creating counter for phrases...\n')
popularity = Counter(phrases)

print ('Few last steps...\n')
with open('PopularPhrases.txt', 'w') as result:
	out = [f'{elem.strip()}\n' for elem in str(popularity)[9:-2].split(',')]
	for elem in out:
		print(str(elem))
	result.writelines(out)
