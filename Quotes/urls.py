from django.conf.urls import patterns, url

urlpatterns = patterns('Quotes.views',
    url(r'^Add/$', 'add_quote_form', name='add-quote'),
    url(r'^Edit/(?P<pID>\d+)/$', 'quote_form', name='edit-quote'),
)