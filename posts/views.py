from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from petspace.permissions import IsOwnerOrReadOnly
from .models import Post
from .models import Category
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('like_post', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'like_post__owner__profile',
        'owner__profile',
        'category',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        """
        New post being created.
        """
        category_name = self.request.data.get('category', None)
        if category_name:
            category = Category.objects.get(name=category_name)
            serializer.save(owner=self.request.user, category=category)
        else:
            serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('like_post', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')