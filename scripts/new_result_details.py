import datetime 
import csv 
from results.models import Result, ResultDetail 

event_id = []

def get_event():
	for e in Result.objects.filter(event__contains="STA Intermediate Singles & Doubles I 2016"):
		event_id.append(e.pk)

def run():
	get_event()
	fields = ['category', 'title', 'name_of_winner']
	for row in csv.reader(open('/Users/liuziyi/documents/norbb/testing-phase/product/mvp/data/sta/results/2016/intermediate_1.csv')):
		result = ResultDetail(**dict(zip(fields,row)))
		result.event_id = event_id[0]
		result.save()