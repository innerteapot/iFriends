from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from iFriends.People.models import Person, Blog
from iFriends.Quotes.models import Quote

# Create your views here.

class EmailForm(forms.Form):
        title = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={'size':'50'}))
        sender = forms.EmailField(max_length=30,
                widget=forms.TextInput(attrs={'size':'30'}))
        date = forms.DateTimeField()
        text = forms.CharField(widget=forms.Textarea(
                                attrs={'rows':'6','cols':'75'}))

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('home/contact_form.html', { 'eForm':eForm })

def home_view(request):
    quotes = Quote.objects.all()
    pList = Person.objects.all()
    bList = Blog.objects.all()
    return render_to_response('home/homepage.html', {
        'quotes': quotes, 'pList': pList, 'bList': bList})

