"""Admin site settings of the 'Bookmarks' application."""

from django.contrib import admin

from bookmarks.models import Bookmark, Collection, UrlType


@admin.register(UrlType)
class UrlTypeAdmin(admin.ModelAdmin):
    """Representation of the UrlType model in the admin panel."""

    list_display = (
        "pk",
        "name",
    )
    search_fields = ("name",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Representation of the Collection model in the admin panel."""

    list_display = (
        "pk",
        "name",
        "description",
        "time_created",
        "time_updated",
        "user",
    )
    search_fields = ("name",)


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """Representation of the Bookmark model in the admin panel."""

    list_display = (
        "pk",
        "title",
        "description",
        "url",
        "url_type",
        "image",
        "time_created",
        "time_updated",
        "user",
    )
    search_fields = ("title",)
