1. Create a .env file containing the ff variables:
    SECRET_KEY
    ALLOWED_HOSTS
    IS_DEBUG
2. Create a superuser account using pipenv run manage createsuperuser
3. Create a stock using the admin.
4. Retrieve a jwt token through the token obtain endpoint ('/api/token/')
    - requires username and password posted
5. Retrieve the stock through the retrieve endpoint ('/api/stocks/')
6. Create an order using the URL of the stock of your choice and set the quantity
    - required payload : {
        'stock': <stock_url>,
        'quantity': <quantitiy_of_the_order>
    }
7. Retrieve orders related to the stock by filtering it using the stock__id filter
    - '/api/orders/?stock__id=<STOCK_ID>'
8. Retrieve the total_investment using the total_investment endpoint
    - 'api/orders/total_investment'
    - you can filter out the total_investment per stock using the stock__id filter.