from django.core.files import storage
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField

from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    pageCount = models.IntegerField(null=True)
    # thumbnailUrl = models.CharField(max_length=256)
    shortDescription = models.CharField(max_length=256)
    longDescription = models.TextField()
    authors = models.ManyToManyField(Author)
    image = models.ImageField(upload_to='images/books/', null=True)

    # default name in admin database
    def __str__(self):
        return f"{self.pk} - {self.title}"

    # fix error in views.py model has no object member
    objects = models.Manager()


class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=CASCADE, null=True)
    image = models.ImageField(
        upload_to='images/review/', null=True, blank=True)
    # image = models.ImageField(null=True)
    # image = models.ImageField(storage=storage.FileSystemStorage(
    #     location='/media/images/review'), null=True)

    def __str__(self):
        return f"{self.user} - {self.body}"
