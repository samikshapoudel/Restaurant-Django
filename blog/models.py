from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from user.models import Custom_user

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/', null=True, blank=True,default='blog/default.jpg')

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    tags = TaggableManager(blank = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name



class Comment(models.Model):
    user = models.ForeignKey(Custom_user, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)



