from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=800)
    bio = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
 

class Location(models.Model):

    event_name = models.CharField(max_length=200, default=1)
    city = models.CharField(max_length=100, default=1)
    state = models.CharField(max_length=100, default=1)
    # link = models.URLField(max_length=300, default=1)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="locations")

    def __str__(self):
        return self.event_name

