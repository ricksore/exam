from rest_framework import viewsets


from .models import Stock
from .serializers import StockSerializer


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read Only ViewSet for stock objects.
    """

    serializer_class = StockSerializer
    queryset = Stock.objects.all()