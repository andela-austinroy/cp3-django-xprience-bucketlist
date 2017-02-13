from rest_framework import serializers
from .models import Bucketlist, BucketlistItem


class BucketlistItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Map model fields onto serializer fields"""
        model = BucketlistItem
        fields = ('id', 'name', 'bucketlist', 'done',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    items = BucketlistItemSerializer(many=True,
                                     read_only=True)

    class Meta:
        """Map model fields onto serializer fields"""
        model = Bucketlist
        fields = ('id', 'name', 'items', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
