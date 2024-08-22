# issaraAssign/urls.py
from django.urls import path
from .views import CarDealerListCreateView, CarDealerRetrieveUpdateDestroyView, UniqueCitiesView

urlpatterns = [
    path('car-dealers/', CarDealerListCreateView.as_view(), name='car-dealer-list-create'),
    path('car-dealers/cities/', UniqueCitiesView.as_view(), name='unique-cities'),
    path('car-dealers/<int:pk>/', CarDealerRetrieveUpdateDestroyView.as_view(), name='car-dealer-detail'),

]
