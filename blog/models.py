from django.db import models

class Blog(models.Model):
    Blog_Title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    Body = models.TextField()
    image = models.ImageField(upload_to='images/')
