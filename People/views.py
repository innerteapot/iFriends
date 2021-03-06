from django.shortcuts import HttpResponse
from People.models import Blog
from People.models import Person
from Quotes.models import Quote
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.vary import vary_on_headers

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title',
            'text',
            'date',
        )


# Create your views here.

@vary_on_headers('User-Agent')
def index(request):
    pList = cache.get('PersonList')
    if pList == None:
        pList = Person.objects.all()
        cache.set('PersonList', pList, 600)
    return render_to_response('people/person_index.html', {'pList': pList})


@login_required
def details(request, pID='0', opts=()):
    rDict = {}
    p = get_object_or_404(Person, pk=pID)
    rDict['p'] = p
    quotes = Quote.objects.all()
    rDict['quotes'] = quotes
    pageLinks = ({'name': 'People', 'value': '/People/'})
    rDict['pageLinks'] = pageLinks
    rDict['showQuotes'] = request.session['show_quotes']
    return render_to_response('people/person_details.html', rDict,
        context_instance = RequestContext(request)
    )


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

@csrf_exempt
def person_form(request, pID='0'):
    class PersonForm(forms.ModelForm):
        class Meta:
            model = Person
            fields = (
                'userID',
                'name',
                'birthday',
                'gender',
                'email',
                'favoriteURL',
                'desc',
                'friends',
                'blogs')

    message = 'Unknown Request'
    p = get_object_or_404(Person, pk=pID)
    #pForm = PersonForm()
    f = PersonForm(instance=p)

    if request.method == 'GET':
        #PersonForm = forms.form_for_instance(p)
        #pForm = PersonForm()
        message = 'Editing person %s ' % p.name

    if request.method == 'POST':
        if request.POST['submit'] == 'update':
            message = 'Update Request for %s.' % p.name
            f = PersonForm(request.POST.copy(), instance=p)

            if f.is_valid():
                message += ' Valid.'
                try:
                      f.save()
                      message += ' Updated.'
                except:
                      message = ' Database Error.'
            else:
                message += ' Invalid.'

    return render_to_response('people/person_form.html', {'pForm':f, 'message': message})


def blog_form(request, pID='0'):
    p = get_object_or_404(Blog, pk=pID)
    pForm = BlogForm(instance=p)
    return render_to_response('people/blog_form.html', {'pForm':pForm})


@csrf_exempt
def add_blog_form(request, pID='0'):
    if not request.user.has_perm('People.can_blog'):
        return HttpResponseRedirect('/')

    if 'session_blog' in request.session:
        return HttpResponseRedirect("/generic/blog_details/%d" %
                     request.session['session_blog'])

    message = 'Unknown Request'
    p = get_object_or_404(Person, userID=request.user)
    bf = BlogForm(instance=p)

    if request.method == 'GET':
        message = 'Add Blog for %s ' % p.name

    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            postDict = request.POST.copy()
            postDict['date'] = datetime.now()
            save_bf = BlogForm(postDict)
            if save_bf.is_valid():
                try:
                    bObj = save_bf.save()
                    p.blogs.add(bObj)
                    p.save()
                    message = 'Blog added to %s.' % p.name
                    request.session['session_blog'] = bObj.id
                except:
                    message = 'Database Error.'
            else:
                message = 'Invalid data in Form.'

    return render_to_response(
        'people/add_blog_form.html',
         {'bForm':bf, 'message': message})

@csrf_exempt
def update_blog(request, bID='0'):
    blog = get_object_or_404(Blog, pk=bID)
    bf = BlogForm(instance=blog)
    message = 'Update Blog'

    if request.method == 'POST':
        if request.POST['submit'] == 'Update':
            blog.title = request.POST['title']
            blog.text = request.POST['text']
            blog.date = datetime.now()
            try:
                blog.save()
                return HttpResponseRedirect("/generic/blog_details/%d" % blog.id)
            except:
                message = 'Database Error.'

    return render_to_response('people/update_blog_form.html',
         {'bForm':bf, 'message': message},
         context_instance = RequestContext(request))

@csrf_exempt
def add_friends(request, pID='0', fID='0'):
    #pID=request.user

    if request.user.has_perm('People.can_add_friends'):
        p = get_object_or_404(Person, userID=pID)
        p.friends.add(fID)

    return HttpResponseRedirect('/')
