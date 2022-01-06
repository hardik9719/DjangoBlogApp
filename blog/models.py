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
    tag_names = models.CharField(max_length=50,primary_key=True)
    tag = models.ManyToManyField(Blog,blank=True)

class TagSearch(models.Model):
    tag_search = models.CharField(max_length=50)

    def __str__(self):
        return self.search

class TagDataForm(ModelForm):
    class Meta:
        model = TagSearch
        fields = '__all__'
        
        widgets = {
            "tag_search" : forms.TextInput(attrs={"class":"form-control"}),
        }


