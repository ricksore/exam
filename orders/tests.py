from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Order
from .views import OrderViewSet
from stocks.models import Stock
from stocks.views import StockViewSet


class OrderTestCase(TestCase):
    """
    TestCases for Order model.
    """

    def setUp(self):

        self.factory = APIRequestFactory()

        self.stock = Stock.objects.create(
            id='GREEN', name='Greenergy Corporation', price=1.50
        )

        self.user = User.objects.create(
            username='test_user', email='test_user@email.com', password='test'
        )

    def _get_stock(self):
        """
        Returns the details of the stock from the RESTful endpoint.
        """

        request = self.factory.get('/api/stocks/')
        force_authenticate(request, user=self.user)
        view = StockViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        return response.data[0]

    def test_order_price_non_mutability(self):
        """
        Asserts the the price of the order is non mutable even if the
        price of the stock changes.
        """

        stock = self._get_stock()

        request = self.factory.post(
            '/api/orders/',
            {'stock': stock['url'], 'quantity': 5},
        )

        previous_price = self.stock.price
        
        force_authenticate(request, user=self.user)
        view = OrderViewSet.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        
        order_id = response.data['id']
        self.stock.price = 3.00
        self.stock.save(update_fields=['price', ])

        # Retrieve the Order again from the retrieve endpoint.
        request = self.factory.get('/api/orders/')
        force_authenticate(request, user=self.user)
        view = OrderViewSet.as_view(actions={'get': 'retrieve'})
        response = view(request, pk=order_id)
        self.assertEqual(response.status_code, 200)

        order_details = response.data
        self.assertNotEqual(order_details['price'], self.stock.price)
        self.assertEqual(order_details['price'], previous_price)