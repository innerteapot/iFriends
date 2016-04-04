from django.shortcuts import render
from django.shortcuts import render_to_response
from People.models import Person
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required
def blog_usage(request):
    pList = Person.objects.all()
    uList = []
    for p in pList:
        size = 0
        for b in p.blogs.all():
            size += b.blog_size()
        uList.append({'person': p,
                      'count': len(p.blogs.all()),
                      'size': size})

    return render_to_response('Custom/blog_usage.html',
                     {'uList': uList},
                     context_instance = RequestContext(request))
