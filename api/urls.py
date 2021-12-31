from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.about, name='api-about'),
    path('blog-list/', views.bloglist, name='blog-list')
]