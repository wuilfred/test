from django import forms

class SubmitTicket(forms.Form):
    url = forms.URLField()