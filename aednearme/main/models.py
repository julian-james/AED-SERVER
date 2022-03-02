from django.db import models
from django.contrib.auth.models import User

class Defib(models.Model):
    ACCESS_CHOICES = [
        ('public', 'public'),
        ('limited', 'limited'),
        ('unknown', 'unknown')
    ]

    address = models.CharField(max_length=255,null=True, blank=True)
    post_code = models.CharField(max_length=7,null=True, blank=True)
    long = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    what3words_link = models.URLField(null=True, blank=True)
    photo_url = models.TextField(null=True, blank=True)
    time_taken = models.DateTimeField(auto_now_add=True)
    access = models.CharField(max_length=50, choices=ACCESS_CHOICES, default='unknown')
    approved = models.BooleanField(default=False)
    comments = models.TextField( null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f'Defib ID: {self.id}, Address: {self.address}, Post Code: {self.post_code}, Longitude: {self.long}, Latitude: {self.lat}, what3words: {self.what3words_link}, Time Taken: {self.time_taken}, User ID: {self.user_id}, Access: {self.access}'