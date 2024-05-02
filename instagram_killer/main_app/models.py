from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=200)
    publish_at = models.DateTimeField(default=now)
    
    def __str__(self) -> str:
        return f"Post: {self.post_text}, {self.publish_at}"