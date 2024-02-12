from django.db import models


class Drink(models.Model):
  """Database model for tracking events"""

  name = models.CharField(max_length=100)
  drink_image = models.URLField()
