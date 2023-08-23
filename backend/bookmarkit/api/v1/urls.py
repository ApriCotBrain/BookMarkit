"""URLs configuration of the 'api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import BookmarkViewSet, CollectionViewSet, UrlTypeViewSet

v1_router = DefaultRouter()

v1_router.register("bookmarks", BookmarkViewSet, basename="bookmark")
v1_router.register("collections", CollectionViewSet, basename="collection")
v1_router.register("urltypes", UrlTypeViewSet, basename="urltype")


urlpatterns = [
    path("", include(v1_router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.authtoken")),
]
