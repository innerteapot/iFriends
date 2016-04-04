from django.conf.urls import patterns, url

urlpatterns = patterns('People.views',
    url(r'^$', 'index', name='people-home'),
    url(r'^Contact/(?P<pID>\d+)/$', 'details'),
    url(r'^Birthday/(?P<pID>\d+)/$', 'details'),
    url(r'^Blog/(?P<pID>\d+)/$', 'blog_form'),
    url(r'^Blogs/(?P<pID>\d+)/$', 'blogs'),
    url(r'^Details/(?P<pID>\d+)/$', 'details', name='people-details'),
    url(r'^Form/(?P<pID>\d+)/$', 'person_form', name='people-form'),
    url(r'^Info/$', 'details'),
    url(r'^Info/(?P<pID>\d+)/$', 'details'),
    url(r'^AddBlogForm/(?P<pID>\d+)/$', 'add_blog_form', name='add-blog'),
    url(r'^AddFriend/(?P<pID>\d+)/(?P<fID>\d+)/$', 'add_friends', name='add-friends'),
    url(r'^UpdateBlog/(?P<bID>\d+)/$', 'update_blog'),
)

