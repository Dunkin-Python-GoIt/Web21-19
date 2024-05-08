from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    publish_at = models.DateTimeField(default=now)
    
    def __str__(self) -> str:
        return f"Post: {self.post_text}, {self.publish_at}"