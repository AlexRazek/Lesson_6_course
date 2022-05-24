from rest_framework import serializers

from skymarket.ads.models import Ad, Comment


class NotAddValidator:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("Cannot add")


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='first_name',
        read_only=True,
    )

    class Meta:
        model = Ad
        fields = ["id", "title", "author", "price", "description", "created_at"]


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "title"]


class CommentDetailSerializer(serializers.ModelSerializer):
    ad = AdSerializer(many=True)

    class Meta:
        model = Comment
        fields = ["id", "title"]


class CommentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id"]

