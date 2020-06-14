from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


########
from rest_framework import pagination
from rest_framework.response import Response


class YourPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })
########


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'title',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer

    def create(self, validated_data):
        post = models.Post(
            slug=validated_data.get('slug'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            author=validated_data.get('author'),
        )
        post.save()
        return post

    class Meta:
        model = models.Post
        fields = ('id', 'slug', 'title', 'description', 'created', 'tags', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'text', 'created', 'tags', 'author')
