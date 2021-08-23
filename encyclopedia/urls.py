from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:caption>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_page/<str:caption>", views.edit_page, name="edit_page"),
    path("random", views.random, name="random"),
    path("tips", views.tips, name="tips"),
]
