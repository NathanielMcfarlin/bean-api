from django.db import models


class OrderedDrink(models.Model):
  """Database model for tracking events"""

  drink = models.ForeignKey("Drink", on_delete=models.CASCADE)
  order = models.ForeignKey("Order", on_delete=models.CASCADE)
  preference = models.ForeignKey("Preference", on_delete=models.CASCADE)