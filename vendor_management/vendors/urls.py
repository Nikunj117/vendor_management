# vendors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorListCreateView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),
    path('purchase_orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:pk>/acknowledge/', views.PurchaseOrderAcknowledgeView.as_view(), name='purchase-order-acknowledge'),
]
