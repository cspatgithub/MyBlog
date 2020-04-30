from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from ckeditor_uploader.fields import RichTextUploadingField


class Project(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='project_cover/' )
    of = models.ForeignKey(User, on_delete=models.CASCADE)
    details = RichTextUploadingField()
    visit_link = models.CharField(default='', max_length=300)
    technology = models.CharField(default='', max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
