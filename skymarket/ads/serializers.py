from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from ads.models import Ad, Comment
from users.models import User

from users.serializers import UserAdSerializer


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='email',
                              queryset=User.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserAdSerializer

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentDetailSerializer(serializers.ModelSerializer):
    author = UserAdSerializer

    class Meta:
        model = Ad
        fields = "__all__"


class CommentListSerializer(serializers.ModelSerializer):
    author = UserAdSerializer
    ad = AdSerializer

    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
