from rest_framework import serializers
from . import models

class BlogSerializer(serializer.ModelSerializer):
    class Meta:
        model = models.Blog 
        fields = ('id', 'name', 'url', 'created_at')

        