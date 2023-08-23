"""URLs configuration of the 'api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    BookmarkViewSet,
    CollectionViewSet,
    UrlTypeViewSet,
    UserViewSet,
)

v1_router = DefaultRouter()

v1_router.register("bookmarks", BookmarkViewSet, basename="bookmarks")
v1_router.register("collections", CollectionViewSet, basename="collections")
v1_router.register("urltypes", UrlTypeViewSet, basename="urltypes")
v1_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(v1_router.urls)),
    path("", include("djoser.urls.authtoken")),
]
