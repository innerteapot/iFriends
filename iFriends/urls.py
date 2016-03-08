from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, WeekArchiveView
from iFriends.People.models import Blog
from iFriends.Quotes.models import Quote

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'iFriends.Home.views.home_view', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^People/', include('iFriends.People.urls')),
    url(r'^Quote/', include('iFriends.Quotes.urls')),
    url(r'^Home/contact/$', 'iFriends.Home.views.contact_view'),
    url(r'^NewUser/$', 'iFriends.Home.views.create_user'),
)

class QuoteList(ListView):
    model = Quote

urlpatterns += patterns('',
    url(r'^generic/quote_list/$', QuoteList.as_view()),
) 

class QuoteCreateView(CreateView):
    model = Quote
    fields = '__all__'
    success_url = '/generic/quote_list'
    template_name = 'Quotes/quote_add.html'

urlpatterns += patterns('',
    url(r'^generic/quote_add/$', csrf_exempt(QuoteCreateView.as_view())),
) 

class QuoteUpdateView(UpdateView):
    model = Quote
    fields = '__all__'
    success_url = '/generic/quote_list'
    template_name = 'Quotes/quote_update.html'

urlpatterns += patterns('',
    url(r'^generic/quote_update/(?P<pk>\d+)/$', csrf_exempt(QuoteUpdateView.as_view())),
) 

class QuoteDeleteView(DeleteView):
    model = Quote
    fields = '__all__'
    success_url = '/generic/quote_list'
    template_name = 'Quotes/quote_delete.html'

urlpatterns += patterns('',
    url(r'^generic/quote_delete/(?P<pk>\d+)/$', csrf_exempt(QuoteDeleteView.as_view())),
) 

class BlogDetail(DetailView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'Blogs/blog_detail.html'
    context_object_name = 'blog'

urlpatterns += patterns('',
    url(r'^generic/blog_details/(?P<pk>\d+)/', BlogDetail.as_view()),
) 

class BlogIndexArchiveView(ArchiveIndexView):
    queryset = Blog.objects.all()
    date_field = "date"
    template_name = 'Blogs/blog_arch.html'
    make_object_list = True
    allow_future = True

urlpatterns += patterns('',
    url(r'^generic/blog_arch/$', BlogIndexArchiveView.as_view()),
)

class BlogYearArchiveView(YearArchiveView):
    queryset = Blog.objects.all()
    date_field = "date"
    template_name = 'Blogs/blog_year.html'
    #make_object_list = True
    allow_future = True

urlpatterns += patterns('',
    url(r'^generic/blog_arch/(?P<year>\d{4})/$',
        BlogYearArchiveView.as_view(),
    )
)

class BlogMonthArchiveView(MonthArchiveView):
    queryset = Blog.objects.all()
    date_field = "date"
    template_name = 'Blogs/blog_month.html'
    #make_object_list = True
    allow_future = True

urlpatterns += patterns('',
    url(r'generic/blog_arch/(?P<year>\d{4})/(?P<month>[a-z]{3})/',
        BlogMonthArchiveView.as_view(),
    )
)

class BlogList(ListView):
    model = Blog
    template_name = 'Blogs/blog_list.html'

urlpatterns += patterns('',
    url(r'^generic/blog_list/$', BlogList.as_view()),
) 

class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    success_url = '/generic/blog_list'
    template_name = 'Blogs/blog_add.html'

urlpatterns += patterns('',
    url(r'^generic/blog_add/$', csrf_exempt(BlogCreateView.as_view())),
) 

class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    success_url = '/generic/blog_list'
    template_name = 'Blogs/blog_update.html'

urlpatterns += patterns('',
    url(r'^generic/blog_update/(?P<pk>\d+)/$', csrf_exempt(BlogUpdateView.as_view())),
) 

class BlogDeleteView(DeleteView):
    model = Blog
    fields = '__all__'
    success_url = '/generic/blog_list'
    template_name = 'Blogs/blog_delete.html'

urlpatterns += patterns('',
    url(r'^generic/blog_delete/(?P<pk>\d+)/$', csrf_exempt(BlogDeleteView.as_view())),
) 

