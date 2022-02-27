from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class TheoryPost(models.Model):
    article = models.CharField(max_length=150)
    content = RichTextField()
    published_time = models.DateTimeField(auto_now=True, auto_created=True)
    count_view = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/theory/post/{self.pk}'

    def __str__(self):
        return self.article
