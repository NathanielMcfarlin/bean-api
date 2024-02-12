from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import permissions
from beanapi.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drink
    fields = ["id", "name", "drink_image"]

class DrinkViewSet(viewsets.ViewSet):
  permission_classes = [permissions.IsAuthenticated]
  def list(self, request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    try:
      drink = Drink.objects.get(pk=pk)
      serializer = DrinkSerializer(drink)
      return Response(serializer.data)
    except Drink.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    name = request.data.get("name")
    drink_image = request.data.get("drink_image")

    drink = Drink.objects.create(
      name=name,
      drink_image=drink_image
    )

    serializer = DrinkSerializer(drink, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def destroy(self, request, pk=None):
        try:
            drink = Drink.objects.get(pk=pk)
            self.check_object_permissions(request, drink)
            drink.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)