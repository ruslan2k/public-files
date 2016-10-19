from django import forms

class ResourceForm(forms.Form):
    resource_name = forms.CharField(label='Resource name', max_length=100)

