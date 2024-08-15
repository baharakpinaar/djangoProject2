from rest_framework import viewsets
from customer.models import Product
from customer.rest.serializers.product import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer