from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django import forms
from django.views.decorators.csrf import csrf_exempt
from iFriends.Quotes.models import Quote

@csrf_exempt
def quote_form(request, pID='0'):
    class QuoteForm(forms.ModelForm): 
        class Meta: 
            model = Quote 
            fields = '__all__'

    message = 'Unknown Request'
    p = get_object_or_404(Quote, pk=pID)
    f = QuoteForm(instance=p)

    if request.method == 'GET':
        message = 'Editing quote'

    if request.method == 'POST':
        if request.POST['submit'] == 'update':
            message = 'Update Request'
            f = QuoteForm(request.POST.copy(), instance=p)

            if f.is_valid():
                message += ' Valid.'
                try:
                      f.save()
                      message += ' Updated.'
                except:
                      message = ' Database Error.'
            else:
                message += ' Invalid.'

    return render_to_response('quotes/quote_form.html', {'pForm':f, 'message': message})


@csrf_exempt
def add_quote_form(request, pID='0'):
    class QuoteForm(forms.ModelForm): 
        class Meta: 
            model = Quote 
            fields = '__all__'

    message = 'Unknown Request'
    bf = QuoteForm()

    if request.method == 'GET':
        message = 'Add Quote'

    if request.method == 'POST':
        if request.POST['submit'] == 'Add':
            save_bf = QuoteForm(request.POST.copy())
            if save_bf.is_valid():
                try:
                    save_bf.save()
                    message = 'Quote added'
                except:
                    message = 'Database Error.'
            else:
                message = 'Invalid data in Form.'

    return render_to_response(
        'quotes/add_quote_form.html',
         {'bForm':bf, 'message': message})

