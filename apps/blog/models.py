from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header = RichTextUploadingField()
    content = RichTextUploadingField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-timestamp']
