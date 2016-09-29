import csv 

from events.models import Event  

def run():
	fields = ['title', 'deadline', 'start_date', 'end_date', 'venue', 'link']

	for row in csv.reader(open('/Users/liuziyi/documents/norbb/testing-phase/product/mvp/data/sta/tournament_duration_split.csv')):
		Event.objects.create(**dict(zip(fields,row)))