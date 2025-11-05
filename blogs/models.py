from django.db import models
from accounts.models import Profile

# Create your models here.
    
class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE ,related_name='author0')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author =models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='author1')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
