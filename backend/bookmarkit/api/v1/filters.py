"""The module contains custom filters"""

from rest_framework import filters


class IsAuthorFilterBackend(filters.BaseFilterBackend):
    """Returns only objects whose author is the user."""

    def filter_queryset(self, request, queryset, view):
        if request.user.is_authenticated:
            return queryset.filter(user=request.user)
        else:
            return queryset.none()
