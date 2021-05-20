from django.db import models
from datetime import datetime


class ShowManager(models.Manager):
    def basic_validator(self, session_data, post_data, all_shows_list):
        errors = {}
        if len(post_data["title"]) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        else:
            session_data["title"] = post_data["title"]
        if post_data["title"].lower() in all_shows_list:
            errors["repeat_title"] = "This show title already exists!"
        else:
            session_data["title"] = post_data["title"]
        if len(post_data["network"]) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        else:
            session_data["network"] = post_data["network"]
        if len(post_data["description"]) > 0 and len(post_data["description"]) < 10:
            errors["description"] = "Show description should be at least 10 characters. Or it can be left empty."
        else:
            session_data["description"] = post_data["description"]
        if not post_data["release_date"] or datetime.strptime(post_data["release_date"], "%Y-%m-%d") > datetime.now():
            errors["release_date"] = "Show release date should be in the past"
        else:
            session_data["release_date"] = post_data["release_date"]
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=20)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"Title: {self.title}; network: {self.network}; release date: {self.release_date}; description: {self.description}"
