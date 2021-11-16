from django.db import models

# Create your models here.
class Plants(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  temperature = models.IntegerField()
  elevation = models.IntegerField()
  pic = models.ImageField(upload_to = 'plants/', default='obviousplant.jpg')

  def __str__(self):
        return f'{self.name}' 