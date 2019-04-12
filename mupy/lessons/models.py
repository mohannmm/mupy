from django.db import models

# Create your models here.
class Publishing(models.Model):
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title

class Content(models.Model):
    lesson_plan = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.lesson_plan
