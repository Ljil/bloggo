from rest_framework import viewsets
from . import (
    serializers,
    models,
    permissons
)


# ljil - Deman666
class PostView(viewsets.ModelViewSet):
    lookup_field = 'slug'
    permission_classes = [
        permissons.IsAuthor
    ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PostDetailSerializer
        return serializers.PostListSerializer

    def get_queryset(self):
        queryset = models.Post.objects.all()
        # Примеры фильтрации
        # http://localhost:8000/api/posts/?tag=IT
        # http://localhost:8000/api/posts/?tag=IT&limit=3
        # http://localhost:8000/api/posts/?tag=PC&tag=MAC
        if self.request.query_params.get('tag'):
            queryset = queryset.filter(tags__title=self.request.query_params.get('tag'))
        if self.request.query_params.get('limit'):
            queryset = queryset[:int(self.request.query_params.get('limit'))]
        return queryset
