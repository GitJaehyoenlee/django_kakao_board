from django.conf import settings
from django.db import models
from blog_board.utils import uuid_name_upload_to

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개 여부')
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)

    # Default Ordering Setting [최신 순 정렬]
    class Meta:
        ordering = ['-id']

class PostImage(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE),
    image = models.ImageField(blank=True, null=True, upload_to='blog/post/%Y/%m/%d')

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)