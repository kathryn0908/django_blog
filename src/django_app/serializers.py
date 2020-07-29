from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog 
        fields = ('id', 'name', 'url', 'created_at')

