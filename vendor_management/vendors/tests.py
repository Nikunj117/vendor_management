# vendors/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder
from django.utils import timezone
from datetime import datetime, timedelta


class VendorManagementTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {
            "name": "Vendor 1",
            "contact_details": "vendor1@example.com",
            "address": "123 Vendor St.",
            "vendor_code": "VEND001"
        }

    def test_create_vendor(self):
        response = self.client.post('/api/vendors/', self.vendor_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_list_vendors(self):
        Vendor.objects.create(**self.vendor_data)
        response = self.client.get('/api/vendors/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_vendor(self):
        vendor = Vendor.objects.create(**self.vendor_data)
        response = self.client.get(f'/api/vendors/{vendor.pk}/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_vendor(self):
        vendor = Vendor.objects.create(**self.vendor_data)
        updated_data = {"name": "Updated Vendor", "contact_details": "updated@example.com", "address": "Updated Address", "vendor_code": "VEND001"}
        response = self.client.put(f'/api/vendors/{vendor.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_vendor(self):
        vendor = Vendor.objects.create(**self.vendor_data)
        response = self.client.delete(f'/api/vendors/{vendor.pk}/', format='json')
        self.assertEqual(response.status_code, 204)
        
class PurchaseOrderTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name="Vendor 2",
            contact_details="vendor2@example.com",
            address="456 Vendor Ave.",
            vendor_code="VEND002"
        )
        self.purchase_order_data = {
            "po_number": "PO001",
            "vendor": self.vendor,
            "order_date": timezone.now(),
            "delivery_date": timezone.now() + timedelta(days=7),
            "items": {"item1": 5, "item2": 10},
            "quantity": 15,
            "status": "pending",
            "issue_date": timezone.now(),
        }

    def test_create_purchase_order(self):
        response = self.client.post('/api/purchase_orders/', {
            **self.purchase_order_data,
            'vendor': self.vendor.pk
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_list_purchase_orders(self):
        PurchaseOrder.objects.create(**self.purchase_order_data)
        response = self.client.get('/api/purchase_orders/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_purchase_order(self):
        po = PurchaseOrder.objects.create(**self.purchase_order_data)
        response = self.client.get(f'/api/purchase_orders/{po.pk}/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_update_purchase_order(self):
        po = PurchaseOrder.objects.create(**self.purchase_order_data)
        updated_data = {
            "po_number": "PO001",
            "vendor": po.vendor.pk,
            "order_date": timezone.now(),
            "delivery_date": timezone.now() + timedelta(days=7),
            "items": {"item1": 5, "item2": 10},
            "quantity": 15,
            "status": "completed",
            "issue_date": timezone.now(),
        }
        response = self.client.put(f'/api/purchase_orders/{po.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_purchase_order(self):
        po = PurchaseOrder.objects.create(**self.purchase_order_data)
        response = self.client.delete(f'/api/purchase_orders/{po.pk}/', format='json')
        self.assertEqual(response.status_code, 204)

    def test_vendor_performance_metrics(self):
        # Create multiple POs for the vendor to simulate different performance metrics
        PurchaseOrder.objects.create(
            po_number="PO002",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=7),
            items={"item1": 5},
            quantity=5,
            status="completed",
            issue_date=timezone.now() - timedelta(days=10),
            acknowledgment_date=timezone.now() - timedelta(days=8),
            quality_rating=4.0
        )
        PurchaseOrder.objects.create(
            po_number="PO003",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=7),
            items={"item1": 5},
            quantity=5,
            status="completed",
            issue_date=timezone.now() - timedelta(days=5),
            acknowledgment_date=timezone.now() - timedelta(days=4),
            quality_rating=5.0
        )
        PurchaseOrder.objects.create(
            po_number="PO004",
            vendor=self.vendor,
            order_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=7),
            items={"item1": 5},
            quantity=5,
            status="canceled",
            issue_date=timezone.now() - timedelta(days=5)
        )

        response = self.client.get(f'/api/vendors/{self.vendor.pk}/performance/', format='json')
        self.assertEqual(response.status_code, 200)
