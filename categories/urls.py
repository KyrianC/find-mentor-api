from django.urls import path

from .views import CategoryNavigation, CategoryList, SubCategoryList

app_name = "categories"

urlpatterns = [
    path("nav/", CategoryNavigation.as_view(), name="nav"),
    path("list/", CategoryList.as_view(), name="list"),
    path("<slug:parent>/", SubCategoryList.as_view(), name="sub_category_list"),
]
