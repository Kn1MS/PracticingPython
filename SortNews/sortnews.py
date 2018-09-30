import re

class New:
	def __init__(self, day=0, month=0, year=0, hour=0, minute=0, contents=''):
		self.day = day
		self.month = month
		self.year = year
		self.hour = hour
		self.minute = minute
		self.contents = contents

	def data_str(self):
		return f'{self.year}.{self.month}.{self.day}, {self.hour}:{self.minute}'

news_strings = []
news_objects = []
tempdatelist = []

with open('News.txt', 'r', encoding='utf-8-sig') as source:
	news_strings = source.read().split('-----------')
	for single_new in news_strings:
		temp_new = New()
		temp_new.contents = single_new
		tempdateline = re.search('\d\d.\d\d.\d\d\d\d', single_new).group()
		tempdatelist = tempdateline.split('.')
		temp_new.day = tempdatelist[0]
		temp_new.month = tempdatelist[1]
		temp_new.year = tempdatelist[2]
		tempdateline = re.search('\d\d:\d\d', single_new).group()
		tempdatelist = tempdateline.split(':')
		temp_new.hour = tempdatelist[0]
		temp_new.minute = tempdatelist[1]
		news_objects.append(temp_new)

news_objects = sorted(news_objects, key=lambda x: x.data_str())

with open('SortedNews.txt', 'w') as result:
	for single_new in news_objects:
		result.write(single_new.contents + '-----------')





