from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from url_filter.integrations.drf import DjangoFilterBackend

from django.db.models import F
from django.db.models import FloatField
from django.db.models import Sum

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Order objects.
    """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['stock', ]

    def get_queryset(self):
        """
        Filter the queryset based from the current orders of the authenticated
        user.
        """

        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """
        Save the current price of the stock on create.
        """

        serializer.save(
            user=self.request.user,
            price=serializer.validated_data['stock'].price
        )

    @action(detail=False, methods=['GET', ], name='Total Investment')
    def total_investment(self, request, *args, **kwargs):
        """
        Endpoint for returning the total investment the User has created for
        a list of stock (or a single stock if a filter was set.)
        """

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        total_investment = queryset.aggregate(
            total_investment=Sum(
                F('price') * F('quantity'),
                output_field=FloatField()
            ),
        )['total_investment']

        response = {
            'total_investment': total_investment,
            'stocks': serializer.data
        }
        return Response(response)