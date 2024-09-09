from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from petspace.permissions import IsOwnerOrReadOnly
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer


class CategoryList(generics.ListAPIView):
    """
    API view to list all categories.
    Allows filtering by name.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]