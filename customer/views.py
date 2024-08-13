from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

# List all customers or create a new customer
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Retrieve, update, or delete a specific customer
class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
