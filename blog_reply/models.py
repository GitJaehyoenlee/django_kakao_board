from django.conf import settings
from django.db import models

# Create your models here.
import blog_board.models


class Comment(models.Model):
    post = models.ForeignKey(blog_board.models.Post, on_delete=models.CASCADE)  # post_id 필드가 생성이 됩니다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reply_likes', blank=True)