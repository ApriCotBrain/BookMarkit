"""Serializers of the 'api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.v1.utils import get_link_info
from bookmarks.models import Bookmark, Collection, UrlType

User = get_user_model()


class UrlTypeSerializer(serializers.ModelSerializer):
    """A serializer for work with url type requests."""

    class Meta:
        fields = ("name",)
        model = UrlType


class CollectionSerializer(serializers.ModelSerializer):
    """A serializer for work with collection requests."""

    class Meta:
        fields = (
            "name",
            "description",
            "time_created",
            "time_updated",
        )
        model = Collection

    def create(self, validated_data):
        current_user = self.context["request"].user
        collection = Collection.objects.create(
            user=current_user, **validated_data
        )
        return collection


class CreateBookmarkSerializer(serializers.ModelSerializer):
    """A serializer for creating bookmarks."""

    collections = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Collection.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        fields = (
            "url",
            "time_created",
            "time_updated",
            "collections",
        )
        model = Bookmark

    def create(self, validated_data):
        current_user = self.context["request"].user
        collections_data = validated_data.pop("collections", [])
        url = validated_data["url"]
        self.validate(validated_data)
        link_info = get_link_info(url)
        og_type = link_info["url_type"]
        url_type, created = UrlType.objects.get_or_create(
            name=og_type, defaults={"name": "website"}
        )

        title = link_info["title"]
        description = link_info["description"]
        image = link_info["image"]

        bookmark = Bookmark.objects.create(
            user=current_user,
            url_type_id=url_type.id,
            title=title,
            description=description,
            image=image,
            **validated_data
        )
        existing_collections = Collection.objects.filter(
            name__in=collections_data
        )
        bookmark.collections.set(existing_collections)
        bookmark.save()

        return bookmark

    def to_representation(self, instance):
        return ReadBookmarkSerializer(instance, context=self.context).data


class ReadBookmarkSerializer(serializers.ModelSerializer):
    """A serializer for reading bookmarks."""

    class Meta:
        fields = (
            "title",
            "description",
            "url",
            "url_type",
            "image",
            "time_created",
            "time_updated",
            "collections",
        )
        model = Bookmark
