from rest_framework import serializers

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


class PostListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Post
        fields = ('id', 'slug', 'title', 'description', 'created', 'tags')


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = models.Post
        fields = ('id', 'title', 'text', 'created', 'tags')
