from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer_list_create'),  # GET: list, POST: create
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),  # GET: retrieve, PUT: update, DELETE: delete
]
