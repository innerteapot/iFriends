from django.conf.urls import patterns, url
from django.views.generic import DetailView
from Quotes.models import Quote

class QuoteDetail(DetailView):
    model = Quote
    queryset = Quote.objects.all()

urlpatterns = patterns('Quotes.views',
    url(r'^Add/$', 'add_quote_form', name='add-quote'),
    url(r'^Edit/(?P<pID>\d+)/$', 'quote_form', name='edit-quote'),
    url(r'^Detail/(?P<pk>\d+)/', QuoteDetail.as_view()),
)

