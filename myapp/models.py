from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
  name = models.CharField('カテゴリ名', max_length=20)
  name_en = models.CharField('カテゴリ名英語', max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def post_count(self):
    n = Post.objects.filter(category = self).count()
    return n

  def __str__(self):
    return self.name

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  title = models.CharField('タイトル', max_length=50)
  content = models.TextField('内容', max_length=990)
  category = models.ForeignKey('Category', on_delete=models.CASCADE)
  thumbnail = models.ImageField(upload_to='images/', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def like_count(self):
    n = Like.objects.filter(post = self).count()
    return n

  def __str__(self):
    return self.title

class Like(models.Model):
  post = models.ForeignKey(Post, verbose_name="投稿", on_delete=models.CASCADE)
  user = models.ForeignKey(User, verbose_name="likeしたユーザー", on_delete=models.CASCADE)

class CustomUser(User):
   class Meta:
    verbose_name_plural = 'CustomUser'