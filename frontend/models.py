from django.db import models
from users.models import User


# Create your models here.


class Booklet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, name="Booklet Name")
    category = models.CharField(max_length=50, null=False, default="Subject")
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
