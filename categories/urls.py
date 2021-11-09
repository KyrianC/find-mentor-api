from django.urls import path

from .views import CategoryNavigation, CategoryList

app_name = "categories"

urlpatterns = [
    path("nav/", CategoryNavigation.as_view(), name="nav"),
    path("list/", CategoryList.as_view(), name="list"),
]
