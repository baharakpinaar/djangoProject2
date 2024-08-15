from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customer.rest.views.customer import CustomerViewset

router = DefaultRouter()
router.register(r'customers', CustomerViewset)

urlpatterns = [
    path('', include(router.urls)),
]