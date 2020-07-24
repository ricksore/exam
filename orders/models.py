from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    """
    Model to hold information of orders initiated by Users.
    
    Prices vary every second so we save the price that the stock was
    bought at the time in this field for historical purpose.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey('stocks.stock', on_delete=models.CASCADE)
    price = models.FloatField(
        help_text='The price at which the stock was bought'
    )
    quantity = models.IntegerField(validators=[
        MinValueValidator(1)
    ])

    def __str__(self):
        return f'{self.stock.name} - {self.quantity} @{self.price}'

    @property
    def total_price(self):
        """
        Returns the multiple of price and quantity.
        """

        return self.price * self.quantity