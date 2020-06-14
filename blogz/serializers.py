from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import request
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

    # {"slug": "ljil_postasdasd2", "title": "ljil_pos2", "description": "ljil_post", "created": "2020-06-14T11:30", "tags":
    # [{"id": 1, "title": "IT"}, {"id": 2, "title": "WEB"}], "author": 1}

    def create(self, validated_data):
        post = models.Post.objects.create(
            **validated_data
        )
        post.save()
        post.tags.set(validated_data.get('tags'))
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
