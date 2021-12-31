from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.blogs, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('input/', views.onTagSubmit, name='createForm'),
    # path('input/submittag/', views.onTagSubmit, name='createForm'),
    # path('input/getData/', views.diplayData, name='display-tagData'),
    # path('input/getTags/', views.showTagData, name='getForm')
]