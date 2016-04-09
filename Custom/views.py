from django.shortcuts import render_to_response
from People.models import Person
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from Log.models import ExceptionEvent, ResponseEvent, RequestEvent, ViewEvent

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

@staff_member_required
def view_log(request, evType='request'):
    if evType == "view":
        lTemplate = 'Custom/view_view_log.html'
        logList = ViewEvent.objects.all()
    elif evType == "response":
        lTemplate = 'Custom/view_response_log.html'
        logList = ResponseEvent.objects.all()
    elif evType == "exception":
        lTemplate = 'Custom/view_exception_log.html'
        logList = ExceptionEvent.objects.all()
    else:
        lTemplate = 'Custom/view_request_log.html'
        logList = RequestEvent.objects.all()

    return render_to_response(lTemplate, {'logList': logList})
