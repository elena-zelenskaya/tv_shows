from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),  # Have your root route redirect to /shows
    path(
        "shows/", views.display_all_shows
    ),  # GET - method should return a template that displays all the shows in a table
    path(
        "shows/new/", views.add_show
    ),  # GET - method should return a template containing the form for adding a new TV show
    path(
        "shows/create/", views.create_show
    ),  # POST - method should add the show to the database, then redirect to /shows/<id>
    path(
        "shows/<int:id>/", views.display_show
    ),  # GET - method should return a template that displays the specific show's information
    path(
        "shows/<int:id>/edit/", views.edit_show
    ),  # GET - method should return a template that displays a form for editing the TV show with the id specified in the url
    path(
        "shows/<int:id>/update/", views.update_show
    ),  # POST - method should update the specific show in the database, then redirect to /shows/<id>
    path(
        "shows/<int:id>/destroy/", views.delete_show
    ),  # POST - method should delete the show with the specified id from the database, then redirect to /shows
]
