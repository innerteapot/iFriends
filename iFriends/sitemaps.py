from django.contrib.sitemaps import Sitemap
from People.models import Person

class PersonSitemap(Sitemap):
    changefreq = "Yearly"
    priority = 0.7
    def items(self):
        return Person.objects.all()

    def location(self, obj):
        return '/Person/info/%d' % obj.id