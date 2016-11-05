from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content')

    def create(self, validated_data):
        """ Create a new post. """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update and return an extant Post with the validated_data. """
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
