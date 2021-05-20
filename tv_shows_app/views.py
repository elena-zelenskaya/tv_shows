from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show
from datetime import datetime

# Create your views here.
def index(request):
    return redirect("/shows/")


def display_all_shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, "index.html", context)


def add_show(request):
    return render(request, "add_show.html")


def create_show(request):
    if request.method == "POST":
        all_shows_list = []
        for show in Show.objects.all():
            all_shows_list.append(show.title.lower())
        errors = Show.objects.basic_validator(request.session, request.POST, all_shows_list)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new/')
        else:
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["release_date"]
            description = request.POST["description"]
            new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
            request.session.flush()
            return redirect(f"/shows/{new_show.id}/")


def display_show(request, id):
    context = {
        "show_to_display": Show.objects.get(id=id),
    }
    return render(request, "display_show.html", context)


def edit_show(request, id):
    context = {
        "show_to_edit": Show.objects.get(id=id),
        "formatted_date_string": Show.objects.get(id=id).release_date.strftime("%Y-%m-%d"),
    }
    return render(request, "edit_show.html", context)



def update_show(request, id):
    if request.method == "POST":
        all_shows_list = []
        for show in Show.objects.all():
            all_shows_list.append(show.title.lower())
        errors = Show.objects.basic_validator(request.session, request.POST, all_shows_list)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{id}/edit/')
        show_to_update = Show.objects.get(id=id)
        if request.POST["title"]:
            show_to_update.title = request.POST["title"]
        if request.POST["network"]:
            show_to_update.network = request.POST["network"]
        if request.POST["release_date"]:
            show_to_update.release_date = request.POST["release_date"]
        if request.POST["description"]:
            show_to_update.description = request.POST["description"]
        show_to_update.save()
        request.session.flush()
        return redirect("../")


def delete_show(request, id):
    show_to_delete = Show.objects.get(id=id)
    show_to_delete.delete()
    return redirect("/")
