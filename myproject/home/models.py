from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title
class student(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)