from django.db import models



class Preference(models.Model):
  """Database model for tracking events"""

  temperature = models.CharField(max_length=100)