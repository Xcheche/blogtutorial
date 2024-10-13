# vim: set fileencoding=utf-8 :
from django.contrib import admin

import blogapp.models as models


class Category1Admin(admin.ModelAdmin):

    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("name",)


class Category2Admin(admin.ModelAdmin):

    list_display = ("id", "name")
    list_filter = ("id", "name")
    search_fields = ("name",)


class PostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "author",
        "title",
        "slug",
        "body",
        "image",
        "first_category",
        "second_category",
        "status",
        "date",
        "number_of_clicks",
    )
    list_filter = (
        "author",
        "first_category",
        "second_category",
        "status",
        "date",
        "id",
        "title",
        "slug",
        "body",
        "image",
        "number_of_clicks",
    )
    search_fields = ("slug",)

    # Prepopulate the 'slug' field using the 'title' field
    prepopulated_fields = {"slug": ("title",)}


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category1, Category1Admin)
_register(models.Category2, Category2Admin)
_register(models.Post, PostAdmin)
