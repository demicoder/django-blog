from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    # author
    # thumbnail

    def __str__(self):
        return self.title

    def truncate_body(self):
        if (len(self.body) > 100):
            return f'{self.body[:100]}...'
        return self.body
