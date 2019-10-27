from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog Admin'


admin.site.register(Post)
