from django.shortcuts import render_to_response
from django import forms
from People.models import Person
from Quotes.models import Quote
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.utils.translation import gettext
from django.utils import translation
from django.contrib.sites.models import Site
from News.models import Story, Announcement
from django.core.cache import cache
from django.views.decorators.cache import cache_control

class EmailForm(forms.Form):
    title = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={'size':'50'}))
    sender = forms.EmailField(max_length=30,
            widget=forms.TextInput(attrs={'size':'30'}))
    date = forms.DateTimeField()
    text = forms.CharField(widget=forms.Textarea(
                                attrs={'rows':'6','cols':'75'}))

gender_list = (('M', 'Male'), ('F', 'Female' ))
class NewUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    first = forms.CharField(max_length=20)
    last = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=gender_list)
    email = forms.EmailField(max_length=30)

siteLanguages = (('en', 'English'), ('de', 'German' ), ('es', 'Spanish'))
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    Language = forms.ChoiceField(choices=siteLanguages)
    quotes   = forms.BooleanField(required=False)

# Create your views here.

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', { 'eForm':eForm })

@cache_control(private=True, max_age=600)
def home_view(request):
    rDict = {}
    pList = cache.get('PersonList')
    if pList == None:
        pList = Person.objects.all()
        cache.set('PersonList', pList, 600)
    rDict['pList'] = pList
    rDict['announceList'] = Announcement.on_site.all()

    currentSite = Site.objects.get_current()
    if (currentSite.domain == 'iFriends.test'):
        hpTemplate = 'home/homepage.html'
        rDict['quotes'] = Quote.objects.all()
    elif (currentSite.domain == 'iNews.test'):
        hpTemplate = 'home/newshomepage.html'
        rDict['storyList'] = Story.on_site.all()

    return render_to_response(hpTemplate, rDict,
                              context_instance = RequestContext(request))

@csrf_exempt
def create_user(request):
    class PersonForm(forms.ModelForm):
        class Meta:
            model = Person
            fields = '__all__'

    message = 'Create New User'
    uForm = NewUserForm()

    if request.method == 'POST':
        if request.POST['submit'] == 'Create':
            postDict = request.POST.copy()
            uForm = NewUserForm(postDict)
            #create User object
            user = User.objects.create_user(postDict['username'],
                                            postDict['email'],
                                            postDict['password'])
            user.last_name = postDict['last']
            user.first_name = postDict['first']
            user.groups.add(Group.objects.get(name='iFriends'))
            user.save()

            #Create a Person object
            perDict = {}
            perDict['name'] = "%s %s" % (postDict['first'], postDict['last'])
            perDict['email'] = postDict['email']
            perDict['gender'] = postDict['gender']
            perDict['favoriteURL'] = 'http://www.iFriends.org'
            perDict['desc'] = 'New User'
            perDict['userID'] = user.id
            pForm = PersonForm(perDict)
            if pForm.is_valid():
                try:
                    p = pForm.save()
                    return HttpResponseRedirect('/People/Info/%d/' % p.id)
                except:
                    message = 'Database Error.'
                    user.delete()
            else:
                message = 'Form Data Error'
                user.delete()

    return render_to_response('registration/create_user.html',{
                'uForm': uForm,
                'message': message })

@csrf_exempt
def login_user(request, next= '/'):
    message = gettext('Login User')
    lForm = LoginForm()

    if request.method == 'GET':
        request.session.set_test_cookie()

    if request.GET.has_key('next'):
        next = request.GET['next']

    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

            if request.POST['submit'] == 'Login':
                postDict = request.POST.copy()
                lForm = LoginForm(postDict)
                if lForm.is_valid():
                    uName = request.POST['username']
                    uPass = request.POST['password']
                    user = authenticate(username=uName, password=uPass)

                    if 'quotes' in request.POST:
                        request.session['show_quotes'] = True
                    else:
                        request.session['show_quotes'] = False

                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            request.session[translation.LANGUAGE_SESSION_KEY] = request.POST['Language']
                            return HttpResponseRedirect(next)
                        else:
                            message = 'Account Deactivated'

                    else:
                        message = 'Login Incorrect'
        else:
            message = "Please enable cookies and try again."

    return render_to_response('registration/login.html',{
                'lForm': lForm,
                'message': message })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/Login')

