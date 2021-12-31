from django.shortcuts import render
# conda install -c conda-forge djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


blogs =[
    {
        'creator':'abc',
        'title':'BTC',
        'blogcontent':'Lorem Ipsum',
        'tags':'BTC CRYP',
        'responses':'Good'
    },
    {
        'creator':'XYZ',
        'title':'ETH',
        'blogcontent':'Lorem Ipsum',
        'tags':'ETH CRYP',
        'responses':'TP'
    },
]
@api_view(['GET'])
def about(request):
    api_urls ={
        'list':'/list_view',
        'create':'/create_view'
    }
    return Response(api_urls)

@api_view(['GET'])
def bloglist(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs)
    context ={'blogs':blogs}
    return render(request,'api/api-about.html',context)
