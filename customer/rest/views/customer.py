from rest_framework import viewsets
from customer.models import Customer
from customer.rest.serializers.customer import CustomerSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer