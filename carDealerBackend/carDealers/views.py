# issaraAssign/views.py
from rest_framework import generics, filters
from .models import CarDealer
from .serializers import CarDealerSerializer
from rest_framework.pagination import CursorPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class CarDealerCursorPagination(CursorPagination):

    page_size = 10  #page size
    ordering = '-popularity'  # Order by popularity dsc

    def paginate_queryset(self, queryset, request, view=None):
        self.total_count = queryset.count()  # Calculate the total count
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'count': self.total_count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class CarDealerListCreateView(generics.ListAPIView):
    queryset = CarDealer.objects.all()
    serializer_class = CarDealerSerializer
    pagination_class = CarDealerCursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'name_en']
    ordering_fields = ['popularity', 'rating_score']

    def get_queryset(self):
        queryset = super().get_queryset()
        city = self.request.query_params.get('city')
        if city:
            queryset = queryset.filter(city=city)
        return queryset

    # get list
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Calculate total count
        total_count = queryset.count()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': total_count,
            'results': serializer.data
        })

class CarDealerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarDealer.objects.all()
    serializer_class = CarDealerSerializer

class UniqueCitiesView(APIView):
    def get(self, request, *args, **kwargs):
        cities = CarDealer.objects.values_list('city', flat=True).distinct()
        return Response(cities)
