"""Viewsets of the 'api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import permissions, mixins, status, viewsets
from rest_framework.response import Response

from api.v1.serializers import (
    CollectionSerializer,
    CreateBookmarkSerializer,
    ReadBookmarkSerializer,
    UrlTypeSerializer,
    UserSerializer,
)
from bookmarks.models import Bookmark, Collection, UrlType

User = get_user_model()


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """A viewset for user creation."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class UrlTypeViewSet(viewsets.ModelViewSet):
    """A viewset for work with url types."""

    queryset = UrlType.objects.all()
    serializer_class = UrlTypeSerializer
    permission_classes = (permissions.IsAdminUser,)
    pagination_class = None


class CollectionViewSet(viewsets.ModelViewSet):
    """A viewset for work with collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = None


class BookmarkViewSet(viewsets.ModelViewSet):
    """A viewset for work with bookmarks."""

    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method in ("POST", "PATCH"):
            return CreateBookmarkSerializer
        return ReadBookmarkSerializer

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
