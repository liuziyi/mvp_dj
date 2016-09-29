from django.conf.urls import include, url

from .views import ResultListView, ResultDetailView

urlpatterns = [
	url(r'^$', ResultListView.as_view(), name='results'),
	url(r'^(?P<pk>\d+)/$', ResultDetailView.as_view(), name='result_detail'),
]