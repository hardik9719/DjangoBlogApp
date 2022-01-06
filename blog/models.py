from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from django import forms
# Create your models here.
class Blog(models.Model):
    blog_creator =models.CharField(max_length=200)
    blog_title =models.CharField(max_length=200)
    blog_details =models.CharField(max_length=200)
    blog_content=models.TextField(blank=True)
    blog_tags=models.CharField(max_length=200)
    blog_responses=models.CharField(max_length=200) #comments
    def __str__(self):
        return self.blog_title

class TagData(models.Model):
    tag_id = models.IntegerField()
    tag = models.ManyToManyField(Blog,blank=True)



class TagDataForm(ModelForm):
    class Meta:
        model = TagData
        fields = ["tag"]
        
        widgets = {
            "tag" : forms.TextInput(attrs={"class":"form-control"}),
        }


