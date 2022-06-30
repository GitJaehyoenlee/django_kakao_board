from django.conf import settings
from django.db import models
from blog_board.utils import uuid_name_upload_to

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='topics', on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='+', on_delete=models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='board_like', blank=True)

    # Default Ordering Setting [최신 순 정렬]
    class Meta:
        ordering = ['-id']

class PostImage(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE),
    image = models.ImageField(blank=True, null=True, upload_to='blog/post/%Y/%m/%d')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # post_id 필드가 생성이 됩니다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reply_like', blank=True)