from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.URLField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "stories"
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        NewsStory,
        on_delete=models.CASCADE, 
        related_name='comments'
        )
    author = models.CharField(max_length=200)
    comment_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text