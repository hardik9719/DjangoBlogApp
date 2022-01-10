from django.core.files.base import ContentFile
from django.http import response
from django.http.request import HttpHeaders
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json

from requests.api import request
# Create your views here.
from .serializer import BlogSerializer
from .models import Blog, TagData, TagSearch
from .models import TagDataForm
import requests
from bs4 import BeautifulSoup





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
def getBlogs(tag_search):
    links =[]
    try:
        response = requests.get("https://medium.com/search?q="+tag_search)
        if response.ok:
            soup = BeautifulSoup(response.content, "html.parser")
            items = soup.find_all("div",class_='postArticle-content',limit=10)
            # print(items)
            for div in items:
                link =  (div.find('a')['href'])
                link = link[:link.find("?source")]
                # print(link)
                links.append(link)
        return links
    except Exception as e:
        print(e)



@csrf_exempt
def onTagSubmit(request):
    form = ""
    links = ""
    context ={}
    if request.method == "POST":
        tag_search = request.POST.dict()['tag_search']
        # # data =  request.POST.items()[1:]
        # # print(request.META['HTTP_X_REQUESTED_WITH'])
        # headers = json.dumps(request.POST)        
        # print((headers))
        # print(type(headers))
        data = TagSearch(tag_search=tag_search)
        data.save()
        links = getBlogs(tag_search)
        form = TagDataForm()
        context['links'] = links
    else:
        form = TagDataForm()

    context['form'] = form

    search_tag_history = TagSearch.objects.all()
    context['tags'] = search_tag_history
    # context = {"form":form,"tags":search_tag_history,"links":links}
    return render(request,"blog/blogs.html",context)
# def diplayData(tag_search):
#     data = TagData.objects.all()
#     context = {'tags':data}
#     return render(request,'blog/blogs.html',context)


