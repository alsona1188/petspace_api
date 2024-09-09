from rest_framework import generics, permissions
from petspace.permissions import IsOwnerOrReadOnly
from like_comment.models import LikeComment
from like_comment.serializers import LikeCommentSerializer


class LikeCommentList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeCommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()