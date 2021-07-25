from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body_text= models.TextField(default=None,blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(default=None, blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True, blank=True)
