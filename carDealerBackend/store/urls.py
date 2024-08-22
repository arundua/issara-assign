from django.urls import path
from .views import KeyValueView

urlpatterns = [
    path('values/', KeyValueView.as_view(), name='key-value'),
]