from django.contrib import admin
from django.db.models import Avg

from .models import Class, ClassRating


class AverageRatingValueFilter(admin.SimpleListFilter):
    title = "average rating"
    parameter_name = "avg_rating"

    def lookups(self, request, model_admin):
        return (
            ("nope", "no rating"),
            (0, "0-25"),
            (25, "25-50"),
            (50, "50-75"),
            (75, "75-100"),
        )

    def queryset(self, request, queryset):
        if self.value() == "nope":
            return queryset.filter(ratings=None)
        elif self.value() is not None:
            value = int(self.value())
            return queryset.annotate(rating_avg=Avg("ratings__value")).filter(
                rating_avg__lt=value + 25, rating_avg__gte=value
            )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "teacher", "basic_price", "average_rating")
    list_filter = ("category", AverageRatingValueFilter, "created", "updated")


@admin.register(ClassRating)
class ClassRatingAdmin(admin.ModelAdmin):
    list_display = (
        "rated_class",
        "author",
        "value",
    )
    list_filter = ("value", "created", "updated")
