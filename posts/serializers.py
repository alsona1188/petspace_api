from rest_framework import serializers
from posts.models import Post
from category.models import Category


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_name = serializers.ReadOnlyField(source='category.name')

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
        allow_null=True,
        required=False
    )

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    def get_category_name(self, obj):
        """
        Retrieves the name of the category linked to the post, if any.
        """
        return obj.category.name if obj.category else None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'image_filter','category', 'category_name',
        ]



