from rest_framework import generics, permissions
from petspace.permissions import IsOwnerOrReadOnly
from like_post.models import LikePost
from like_post.serializers import LikePostSerializer


class LikePostList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikePostSerializer
    queryset = LikePost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikePostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikePostSerializer
    queryset = LikePost.objects.all()