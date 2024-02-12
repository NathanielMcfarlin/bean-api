from rest_framework import viewsets, status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import permissions
from beanapi.models import Order, OrderedDrink

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'datetime', 'purchased']

class OrdersViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

    def create(self, request, *args, **kwargs):
        # Set the purchased field to False explicitly
        request.data['purchased'] = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Order.objects.filter(user=user, purchased=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = request.user 
        order = Order.objects.get(user=user, purchased = False)

        order.purchased = True
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = request.user

        order = Order.objects.get(
            user=user,
            purchased=False,
        )
        self.perform_destroy(order)
        return Response(status=status.HTTP_204_NO_CONTENT)

# ! ------------------------- ordered drink viewset -------------------------------------------

class OrderedDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedDrink
        fields = ['id', 'drink', 'order', 'preference']

class OrderedDrinkViewSet(viewsets.ModelViewSet):
    queryset = OrderedDrink.objects.all()
    serializer_class = OrderedDrinksSerializer

    def create(self, request, *args, **kwargs):
        user = request.user 

        # Get or create an order for the current user
        order, created = Order.objects.get_or_create(
            user=user,
            purchased=False,
        )

        # Associate the created order with the ordered drink
        request.data['order'] = order.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = OrderedDrink.objects.filter(order__user=user, order__purchased=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            ordered_drink = self.get_object()
            ordered_drink.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# ! --------------------------------------------------- CART VIEWSET -------------------------------------------------------------------------------------------------------------
        

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'datetime', 'purchased']

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Order.objects.filter(user=user, purchased=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# !----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
class PastOrderedDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedDrink
        fields = ['id', 'drink', 'order', 'preference']

class PastOrderedDrinkViewSet(viewsets.ModelViewSet):
    queryset = OrderedDrink.objects.all()
    serializer_class = OrderedDrinksSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = OrderedDrink.objects.filter(order__user=user, order__purchased=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)