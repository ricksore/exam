from rest_framework import serializers

from .models import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Stock model.
    """
    
    class Meta:
        model = Stock
        fields = ['url', 'id', 'name', 'price']