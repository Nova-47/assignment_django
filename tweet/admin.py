from django.contrib import admin
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk Filter"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("contains", "Contains 'Elon Musk'"),
            ("not_contains", "Doesn't contain 'Elon Musk'"),
        )

    def queryset(self, request, queryset):
        if self.value() == "contains":
            return queryset.filter(payload__icontains="Elon Musk")
        if self.value() == "not_contains":
            return queryset.exclude(payload__icontains="Elon Musk")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "tweet", "created_at")
    search_fields = ("user__username",)
    list_filter = ("created_at",)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "user", "created_at")
    search_fields = ("payload", "user__username")
    list_filter = ("created_at", ElonMuskFilter)
