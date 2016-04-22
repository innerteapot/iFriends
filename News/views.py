from models import Announcement, Story
from django.views.generic import DetailView, ListView
from iFriends import settings

class AnnouncementDetail(DetailView):
    #model = Announcement
    queryset = Announcement.objects.filter(sites=settings.SITE_ID)

class AnnouncementList(ListView):
    model = Announcement

class StoryDetail(DetailView):
    #model = Story
    queryset = Story.objects.filter(site=settings.SITE_ID)

class StoryList(ListView):
    model = Story
