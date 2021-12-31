from django.db.models import fields
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        blog = Blog
        fields = '__all__'