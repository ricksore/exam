from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.HyperLinkedSerializer):
    """
    Serializer for Order model.
    """

    class Meta:
        model = Order
        fields = ['user', 'stock', 'price', 'quantity', ]
        read_only_fields = ['price', ]
