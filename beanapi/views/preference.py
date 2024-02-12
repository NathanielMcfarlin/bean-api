from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import permissions
from beanapi.models import Preference

class PreferenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Preference
    fields = ["id", "temperature"]

class PreferenceViewSet(viewsets.ViewSet):
  permission_classes = [permissions.IsAuthenticated]
  def list(self, request):
    preferences = Preference.objects.all()
    serializer = PreferenceSerializer(preferences, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    try:
      preference = Preference.objects.get(pk=pk)
      serializer = PreferenceSerializer(preference)
      return Response(serializer.data)
    except Preference.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    
  def create(self, request):
    temperature = request.data.get("temperature")

    preference = Preference.objects.create(
      temperature=temperature
    )

    serializer = PreferenceSerializer(preference, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def destroy(self, request, pk=None):
        try:
            preference = Preference.objects.get(pk=pk)
            self.check_object_permissions(request, preference)
            preference.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Preference.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)