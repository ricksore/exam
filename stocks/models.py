from django.db import models


class Stock(model.Model):
    """
    Model for storing stocks and their current price.
    """

    id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    
    def __str__(self):
        return f'{self.name} - {self.id}'