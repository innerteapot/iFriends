from django.conf.urls import patterns, include, url

details1 = {'opts':('name','email')}
details2 = {'opts':('name','birthday')}
details3 = {'opts':('name','desc','favoriteURL')}

urlpatterns = patterns('iFriends.People.views',
    url(r'^$', 'index'),
    url(r'^Contact/(?P<pID>\d+)/$', 'details', details1),
    url(r'^Birthday/(?P<pID>\d+)/$', 'details', details2),
    url(r'^Blogs/(?P<pID>\d+)/$', 'blogs'),
    url(r'^Details/(?P<pID>\d+)/$', 'details', details3),
    url(r'^Info/$', 'details'),
    url(r'^Info/(?P<pID>\d+)/$', 'details'),
    url(r'^(?P<name>\w+)/$', 'index'),
)

