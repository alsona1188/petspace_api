from rest_framework import serializers
from likes.models import LikePost


class LikePostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikePost
        fields = ['id', 'created_at', 'owner', 'post']