from django.db import models
from users.models import User


# Create your models here.

class Booklet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, name="Booklet Name")
    category = models.CharField(max_length=50, choices=[
        "Math",
        "Geometry",
        "Physics",
        "Biology",
        "Chemistry",
        "Literature",
        "Writing",
        "Linguistic",
        "GeopGraphy",
        "English",
        "Arabic",
        "Theology",
        "Quran",
        "Social Studies",
        "Computer",
        "Social Media Intelligence",
        "Technology",
    ], null=False, default="Subject")
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    booklet_file = models.FileField(upload_to='booklets/')

    def __str__(self):
        return self.name


class Journal(models.Model):
    author = 1
    name = models.CharField(max_length=100, null=False, name="Booklet Name")
    category = models.CharField(max_length=50, choices=[
        "Physics",
        "Movie and comic",
        "Hello copter",
        "Biology and Chemistry",
        "Computer",
        "Philosophy",
        "Writing",
    ], null=False, default="Subject")
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    booklet_file = models.FileField(upload_to='journals/')
