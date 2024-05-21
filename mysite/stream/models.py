from django.db import models

# Create your models here.
class Stream(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

