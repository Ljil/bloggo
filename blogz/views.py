from rest_framework import viewsets
from . import (
    serializers,
    models
)


class PostView(viewsets.ModelViewSet):
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PostDetailSerializer
        return serializers.PostListSerializer

    def get_queryset(self):
        queryset = models.Post.objects.all()
        if self.request.query_params.get('tag'):
            queryset = queryset.filter(tags__title=self.request.query_params.get('tag'))
        if self.request.query_params.get('limit'):
            queryset = queryset[:int(self.request.query_params.get('limit'))]
        return queryset
