from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from django import forms
# Create your models here.
class Blog(models.Model):
    creator =models.CharField(max_length=200)
    title =models.CharField(max_length=200)
    details =models.CharField(max_length=200)
    blogcontent=models.CharField(max_length=20000)
    tags=models.CharField(max_length=200)
    responses=models.CharField(max_length=200) #comments
    def __str__(self):
        return self.title

class TagData(models.Model):
    tag = models.CharField(max_length=20,name="tag")

    def __str__(self):
        return self.tag



class TagDataForm(ModelForm):
    class Meta:
        model = TagData
        fields = ["tag"]
        
        widgets = {
            "tag" : forms.TextInput(attrs={"class":"form-control"}),
        }


