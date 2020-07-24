from rest_framework import viewsets


from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModeViewSet):
    """
    ViewSet for Order objects.
    """

    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Filter the queryset based from the current orders of the authenticated
        user.
        """

        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Save the current price of the stock on create.
        """

        serializer.save(price=serializer.validated_data['stock'])