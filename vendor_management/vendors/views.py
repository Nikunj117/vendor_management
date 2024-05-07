# vendors/views.py
from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, views
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id:
            return PurchaseOrder.objects.filter(vendor__id=vendor_id)
        return PurchaseOrder.objects.all()


class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class VendorPerformanceView(views.APIView):
    def get(self, request, pk):
        vendor = get_object_or_404(Vendor, pk=pk)

        # Calculate On-Time Delivery Rate
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=models.F('order_date'))
        on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders else 0.0

        # Calculate Quality Rating Average
        quality_ratings = completed_orders.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
        quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0.0

        # Calculate Average Response Time
        acknowledgment_times = completed_orders.exclude(acknowledgment_date__isnull=True).values_list('issue_date', 'acknowledgment_date')
        response_times = [(ack[1] - ack[0]).total_seconds() for ack in acknowledgment_times]
        average_response_time = sum(response_times) / len(response_times) if response_times else 0.0

        # Calculate Fulfillment Rate
        fulfilled_orders = completed_orders.filter(status='completed')
        fulfillment_rate = (fulfilled_orders.count() / completed_orders.count()) * 100 if completed_orders else 0.0

        # Update Vendor Performance Metrics
        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = quality_rating_avg
        vendor.average_response_time = average_response_time
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()

        return Response({
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }, status=status.HTTP_200_OK)


class PurchaseOrderAcknowledgeView(views.APIView):
    def post(self, request, pk):
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        purchase_order.acknowledgment_date = request.data.get('acknowledgment_date')
        purchase_order.save()

        # Update Vendor Performance Metrics
        vendor = purchase_order.vendor
        VendorPerformanceView().get(request, vendor.id)

        return Response({'message': 'Acknowledgment Date Updated'}, status=status.HTTP_200_OK)
