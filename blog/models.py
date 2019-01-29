from django.db import models

class Blog(models.Model):
    Blog_Title = models.Charfield("Troy's Blog!!")
    pub_date = models.DateField(pub_date)
    Body = models.Charfield(max_length=200)
    image = models.ImageField(upload_to='images/')
    
