from django.db import models
from users.models import User

ADMIN = User.objects.get(id=1)


# Create your models here.

class Booklet(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET(ADMIN))
    name = models.CharField(max_length=100, null=False, name="Booklet Name")
    category = models.CharField(max_length=50, choices=[
        ("Math", "Math"),
        ("Geometry", "Geometry"),
        ("Physics", "Physics"),
        ("Biology", "Biology"),
        ("Chemistry", "Chemistry"),
        ("Literature", "Literature"),
        ("Writing", "Writing"),
        ("Linguistic", "Linguistic"),
        ("GeopGraphy", "GeopGraphy"),
        ("English", "English"),
        ("Arabic", "Arabic"),
        ("Theology", "Theology"),
        ("Quran", "Quran"),
        ("Social Studies", "Social Studies"),
        ("Computer", "Computer"),
        ("Social Media Intelligence", "Social Media Intelligence"),
        ("Technology", "Technology"),
    ], null=False, default="Subject")
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    booklet_file = models.FileField(upload_to='booklets/', blank=True)

    def __str__(self):
        return f"Booklets, {self.name}: {self.category}"


class Journal(models.Model):
    author = ADMIN
    name = models.CharField(max_length=100, null=False, name="Booklet Name")
    category = models.CharField(max_length=50, choices=[
        ("Physics", "Physics"),
        ("Movies and comics", "Movies and comics"),
        ("Helli copter", "Helli copter"),
        ("Biology and Chemistry", "Biology and Chemistry"),
        ("Computer", "Computer"),
        ("Philosophy", "Philosophy"),
        ("Writing", "Writing"),
    ], null=False, default="Subject")
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    journal_file = models.FileField(upload_to='journals/', blank=True)

    def __str__(self):
        return f"Journals, {self.name}: {self.category}"
