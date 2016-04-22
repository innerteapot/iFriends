from django.conf.urls import patterns, url
#from django.views.decorators.csrf import csrf_exempt
import views

urlpatterns = patterns('',
    url(r'^Announcement/$', views.AnnouncementList.as_view()),
    url(
            r'^Announcement/Detail/(?P<pk>[0-9]+)/$',
            views.AnnouncementDetail.as_view(),
            name='announcement-detail'
        ),
    url(r'^Story/$', views.StoryList.as_view()),
    url(
            r'^Story/Detail/(?P<pk>[0-9]+)/$',
            views.StoryDetail.as_view(),
            name='story-detail'
        ),
)
