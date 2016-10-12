from django import forms

class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', max_length=100)


