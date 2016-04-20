from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView
from People.models import Blog
from Quotes.models import Quote
from sitemaps import PersonSitemap
from django.contrib.sitemaps import GenericSitemap

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Home.views.home_view', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/view_log/(?P<evType>\w+)/$', 'Custom.views.view_log'),
    url(r'^admin/logout/$', 'Home.views.logout_user'),
    url(r'^admin/blog_usage/$', 'Custom.views.blog_usage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^People/', include('People.urls')),
    url(r'^Quote/', include('Quotes.urls')),
    url(r'^Home/contact/$', 'Home.views.contact_view'),
    url(r'^NewUser/$', 'Home.views.create_user'),
    url(r'^Login/$', 'Home.views.login_user'),
    url(r'^Logout/$', 'Home.views.logout_user'),
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

blog_detail_info = {
    'queryset' : Blog.objects.all(),
    'date_field' : 'date',
    'template_object_name': 'blog',
    'template_name' : 'Blogs/blog_detail.html',
}

quote_detail_info = {
    'queryset' : Quote.objects.all(),
    'date_field' : 'date',
    'template_object_name': 'quote',
    'template_name' : 'Quotes/quote_detail.html',
}

sitemaps = {
    'person': PersonSitemap,
    'blog': GenericSitemap(blog_detail_info, priority=0.3,
                           changefreq='weekly'),
    'quote': GenericSitemap(quote_detail_info, priority=0.3,
                           changefreq='weekly'),
}

urlpatterns += patterns('',
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap',
                        {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+).xml$',
   'django.contrib.sitemaps.views.sitemap',
                        {'sitemaps': sitemaps}),
)