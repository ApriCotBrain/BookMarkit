"""Viewsets of the 'api' application v1."""

from django.contrib.auth import get_user_model
from rest_framework import permissions, mixins, status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from api.v1.filters import IsAuthorFilterBackend
from api.v1.serializers import (
    CollectionSerializer,
    CreateBookmarkSerializer,
    ReadBookmarkSerializer,
    UrlTypeSerializer,
    UserSerializer,
)
from bookmarks.models import Bookmark, Collection, UrlType
from core.enums import Limits

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


class CollectionViewSet(viewsets.ModelViewSet):
    """A viewset for work with collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_backends = (IsAuthorFilterBackend,)
    pagination_class = PageNumberPagination
    pagination_class.page_size = Limits.COLLECTION_NUMBER_PER_PAGE


class BookmarkViewSet(viewsets.ModelViewSet):
    """A viewset for work with bookmarks."""

    queryset = Bookmark.objects.all()
    serializer_class = CreateBookmarkSerializer
    filter_backends = (IsAuthorFilterBackend,)
    pagination_class = PageNumberPagination
    pagination_class.page_size = Limits.BOOKMARK_NUMBER_PER_PAGE

    def get_serializer_class(self):
        if self.request.method in ("POST", "PATCH"):
            return CreateBookmarkSerializer
        return ReadBookmarkSerializer

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
