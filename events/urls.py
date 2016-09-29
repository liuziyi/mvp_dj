from django.conf.urls import include, url

from .views import EventListView

urlpatterns = [
	url(r'^$', EventListView.as_view(), name='events'),
]