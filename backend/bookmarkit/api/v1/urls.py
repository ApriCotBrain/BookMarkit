"""URLs configuration of the 'api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import BookmarkViewSet, CollectionViewSet, UrlTypeViewSet

router = DefaultRouter()

router.register("bookmarks", BookmarkViewSet, basename="bookmark")
router.register("collections", CollectionViewSet, basename="collection")
router.register("urltypes", UrlTypeViewSet, basename="urltype")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
