from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from .models import KeyValue
from .serializers import KeyValueSerializer
from datetime import timedelta

class KeyValueView(generics.GenericAPIView):
    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer

    def get(self, request, *args, **kwargs):
        keys = request.query_params.get('keys', None)
        response_data = {}

        if keys:
            keys_list = keys.split(',')
            for key in keys_list:
                key_value = get_object_or_404(KeyValue, key=key)
                if key_value.is_expired():
                    key_value.delete()
                else:
                    key_value.reset_ttl()
                    response_data[key] = key_value.value
        else:
            # Remove expired values
            KeyValue.objects.filter(created_at__lt=timezone.now() - timedelta(minutes=5)).delete()
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            response_data = {item['key']: item['value'] for item in serializer.data}

        return Response(response_data)

    def post(self, request, *args, **kwargs):
        for key, value in request.data.items():
            key_value, created = KeyValue.objects.update_or_create(
                key=key, defaults={'value': value, 'created_at': timezone.now()}
            )
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        for key, value in request.data.items():
            key_value = get_object_or_404(KeyValue, key=key)
            key_value.value = value
            key_value.reset_ttl()
            key_value.save()
        return Response(status=status.HTTP_200_OK)
