from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from iFriends.People.models import Person, Blog
from iFriends.Quotes.models import Quote
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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
        password = forms.CharField(max_length=20,
                                   widget=forms.PasswordInput())
        first = forms.CharField(max_length=20)
        last = forms.CharField(max_length=20)
        gender = forms.ChoiceField(choices=gender_list)
        email = forms.EmailField(max_length=30)

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', { 'eForm':eForm })

def home_view(request):
    quotes = Quote.objects.all()
    pList = Person.objects.all()
    bList = Blog.objects.all()
    return render_to_response('home/homepage.html', {
        'quotes': quotes, 'pList': pList, 'bList': bList})

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


