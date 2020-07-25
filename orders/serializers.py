from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Order model.
    """

    class Meta:
        model = Order
        fields = ['url', 'stock', 'price', 'quantity', ]
        read_only_fields = ['price', ]
