from rest_framework import serializers


class FavoriteSerializer(serializers.Serializer):
    product = serializers.CharField()


class CommentSerializer(serializers.Serializer):
    user = serializers.EmailField()
    comment = serializers.CharField()
    product = serializers.CharField()


class FanSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)


class ReviewerSerializer(serializers.Serializer):
    user = serializers.CharField()
    rating = serializers.IntegerField()
