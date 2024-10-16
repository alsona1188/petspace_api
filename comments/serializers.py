from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from like_comment.models import LikeComment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    like_id_comment = serializers.SerializerMethodField()
    likes_count_comment = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    def get_like_id_comment(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like_comment = LikeComment.objects.filter(
                owner=user, comment=obj
            ).first()
            return like_comment.id if like_comment else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'description',
            'like_id_comment', 'likes_count_comment']


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
    