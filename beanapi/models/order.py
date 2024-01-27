from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
  """Database model for tracking events"""

  datetime = models.DateField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
