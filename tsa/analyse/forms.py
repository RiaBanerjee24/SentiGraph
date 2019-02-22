from django import forms

class HomeForm(forms.Form):
    Hashtag = forms.CharField(max_length=50)