from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Blogger(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse("blogger-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    contents = models.TextField()
    author = models.ForeignKey(Blogger,on_delete=models.CASCADE,related_name='comment_author')
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return f'{self.author}'

class Post(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Blogger,on_delete=models.CASCADE,related_name='post_author')
    contents = models.TextField()
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='post_comment',blank=True, null=True)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    


    