from rest_framework import serializers
from .models import Category
from rest_framework import generics


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_on']


class CategoryDetailSerializer(CategorySerializer):
    """
    Serializer for Comment model in Detail view
    """
    category_id = serializers.ReadOnlyField(source='id')

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_on', 'category_id']