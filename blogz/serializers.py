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

    # {
    #     "slug": "a3332",
    #     "title": "ljil_pos2",
    #     "description": "ljil_post",
    #     "text": "123",
    #     "tags": [
    #         {
    #             "id": 1,
    #             "title": "IT"
    #         },
    #         {
    #             "id": 2,
    #             "title": "WEB"
    #         },
    #         {
    #             "id": 3,
    #             "title": "PC"
    #         },
    #         {
    #             "id": 4,
    #             "title": "MAC"
    #         },
    #         {
    #             "id": 5,
    #             "title": "PYTHON"
    #         }
    #     ],
    #     "author": 1
    # }

    def create(self, validated_data):
        post = models.Post.objects.create(
            slug=validated_data.get('slug'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            text=validated_data.get('text'),
            author=validated_data.get('author')
        )
        post.save()

        for tag in validated_data.get('tags'):
            tag_to_add = models.Tag.objects.get(title=tag['title'])
            post.tags.add(tag_to_add)
        return post

    class Meta:
        model = models.Post
        fields = ('id', 'slug', 'title', 'description', 'text', 'created', 'tags', 'author')


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = UserSerializer

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'text', 'created', 'tags', 'author')
