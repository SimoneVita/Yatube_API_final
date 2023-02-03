from rest_framework.serializers import (
    ModelSerializer, ValidationError, CurrentUserDefault)
from rest_framework.relations import (
    SlugRelatedField, StringRelatedField)
from rest_framework.validators import UniqueTogetherValidator
from posts.models import (
    Comment, Post, Group, Follow, User)


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('id', 'author', 'post', 'created',)
        model = Comment


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    comments = CommentSerializer(
        many=True, required=False
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'id', 'pub_date', 'comments',)
        model = Post


class GroupSerializer(ModelSerializer):
    title = StringRelatedField(
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(ModelSerializer):
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username', required=True
    )
    user = SlugRelatedField(
        read_only=True, slug_field='username', default=CurrentUserDefault()
    )

    class Meta:
        fields = ('user', 'following',)
        read_only_fields = ('user',)
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Уже есть подписка!'
            )
        ]

    def validate_following(self, value):
        if value == self.context.get('request').user:
            raise ValidationError(
                'Подписаться на себя можно только Бузовой!'
            )
        return value
