from django.db import models

class Professional(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Location(models.Model):

    venue = models.CharField(max_length=300)
    bio = models.TextField(max_length=800)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name="locations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.venue

