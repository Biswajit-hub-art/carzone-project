from django.db import models

# Create your models here.

class Team(models.Model):
    first_name= models.CharField(max_length=300, blank=False)
    last_name= models.CharField(max_length=255, blank=False)
    designation= models.CharField(max_length=255, blank=False)
    photo= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    facebook_link= models.URLField(max_length=255)
    twitter_link= models.URLField(max_length=255)
    google_plus_link= models.URLField(max_length=255)
    created_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
