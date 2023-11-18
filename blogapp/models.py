from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatar/')

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Coments(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.message[:10]


class Post(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/')
    like = models.ManyToManyField(User, related_name='like', null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def num_of_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sin_blog', kwargs={'pk': str(self.pk)})
