from rest_framework import serializers
from .models import Todo, User, Photo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_user', 'is_admin')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'content', 'completed', 'user', 'timestamp', 'updated')

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'user', 'title', 'description', 'image', 'timestamp', 'updated')
