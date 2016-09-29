from datetime import datetime 

from events.models import Event 
from results.models import Result 

today = datetime.now()

def run():
	for event in Event.objects.filter(start_date__year=2016).exclude(start_date__gt=today):
		Result.objects.create(event=event.title, date=event.start_date)