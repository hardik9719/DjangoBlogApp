from django import forms

class GetTags(forms.Form):
    tag = forms.CharField(label="Tag",max_length=20)
