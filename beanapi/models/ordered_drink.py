from django.db import models


class OrderedDrink(models.Model):
  """Database model for tracking events"""

  drink = models.ForeignKey("Drink", on_delete=models.CASCADE)