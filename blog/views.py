from django.core.files.base import ContentFile
from django.http import response
from django.http.request import HttpHeaders
from django.shortcuts import render
from .models import Blog, TagData, TagSearch
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json
# Create your views here.
from .serializer import BlogSerializer
from .models import TagDataForm





posts=[
    {
        'creator':'CoreyMS',
        'title':'Future of Cyer security',
        'details':'5th May 5 min read',
        'content':'XYZ',
        'tags':'Eth,btc etc',
        'responses':'comments'
    },
    {
        'creator':'My',
        'title':'Future of Ty security',
        'details':'5th May 5 min read',
        'content':'XYZ',
        'tags':'Eth,btc etc',
        'responses':'comments'
    }
]


def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request,'blog/about.html')

def blogs(request):
    posts = Blog.objects.all()
    context = {'blogs':posts}
    return render(request,'blog/bloglist.html',context)


@csrf_exempt
def onTagSubmit(request):
    form = ""
    if request.method == "POST":
        tag_search = request.POST.dict()['tag_search']
        # # data =  request.POST.items()[1:]
        # # print(request.META['HTTP_X_REQUESTED_WITH'])
        # headers = json.dumps(request.POST)        
        # print((headers))
        # print(type(headers))
        data = TagSearch(tag_search=tag_search)
        data.save()
        form = TagDataForm()
    else:
        form = TagDataForm()

    all_tags = TagData.objects.all()
    context = {"form":form,"tags":all_tags}
    return render(request,"blog/blogs.html",context)
# def diplayData(request):
#     data = TagData.objects.all()
#     context = {'tags':data}
#     return render(request,'blog/blogs.html',context)

