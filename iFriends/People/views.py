from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from iFriends.People.models import Person

def index(request, name=''):
    response = HttpResponse()

    response.write("<html><body>\n")
    response.write("<h1>People</h1><hr>")
    pList = Person.objects.all()
    for p in pList:
        link = "<a href=\"Info/%d\">" % (p.id)
        response.write("<li>%s%s</a></li>" % (link, p.name))
    response.write("</body></html>")

    return response


def details(request, pID='0', opts=()):
    response = HttpResponse()

    response.write("<html><body>\n")
    try:
        p = Person.objects.get(id=pID)
        response.write("<h1>Details for Person %s</h1><hr>\n" % p.name)
        for d in opts:
            response.write("<li>%s: %s</li>" % (d, p.__dict__[d]))
    except Person.DoesNotExist:
        response.write("Person Not Found")
    response.write("</body></html>")

    return response

def blogs(request, pID='0'):
    response = HttpResponse()

    response.write("<html><body>\n")
    try:
        p = Person.objects.get(id=pID)
        response.write("<h1>Blogs for Person %s</h1><hr>\n" % p.name)
        for b in p.blogs.all():
            response.write("<li>%s</li>" % (b.title))
    except Person.DoesNotExist:
        response.write("Person Not Found")
    response.write("</body></html>")

    return response
