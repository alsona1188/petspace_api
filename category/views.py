from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from petspace.permissions import IsOwnerOrReadOnly
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryList(generics.ListCreateAPIView):
    """
    API view to list all categories.
    Allows filtering by name.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def perform_create(self, serializer):
        """
        Custom logic to create a new category.
        Optionally, associate the category with the logged-in user.
        """
        # Save the new category associated with the logged-in user
        serializer.save()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]