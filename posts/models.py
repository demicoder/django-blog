from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # author
    # thumbnail
