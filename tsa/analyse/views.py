from django.shortcuts import render
from . import forms
from . import logic
def get(request):
    form = forms.HomeForm()
    return render(request,'analyse/home.html',{'form':form})

def post(request):
    form = forms.HomeForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data['Hashtag']
        result = logic.logicBox(query)
        args = {'tweetText':result[0], 'pos': result[1], 'neutral': result[2], 'neg': result[3]}
        return render(request,'analyse/results.html',args)

