# Vendor Management System

## Overview

The Vendor Management System is a tool for handling vendor profiles, tracking purchase orders, and calculating vendor performance metrics. This project is built using Django and Django REST Framework and adheres to RESTful API principles.

## Features

- **Vendor Profile Management**
- **Purchase Order Tracking**
- **Vendor Performance Evaluation**

### Core Features

1. **Vendor Profile Management:**
   - Create, retrieve, update, and delete vendor profiles.

2. **Purchase Order Tracking:**
   - Manage and track purchase orders with detailed item information.

3. **Vendor Performance Evaluation:**
   - Calculate metrics like On-Time Delivery Rate, Quality Rating, Response Time, and Fulfillment Rate.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8+ (recommended)
- Virtual environment tool (`venv` or `virtualenv`)
- Git

### Clone Repository

1. Clone the repository:
   ```bash
    git clone <REPO_URL>
    cd <REPO_DIRECTORY>

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux or Mac
    venv\Scripts\activate     # Windows

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    
4. Run migrations to set up the database schema:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser

6. Start the Django development server:
    ```bash
    python manage.py runserver

# Usage    
## API Endpoints
### Vendor API Endpoints

- POST /api/vendors/: Create a new vendor
- GET /api/vendors/: List all vendors
- GET /api/vendors/{pk}/: Retrieve a specific vendor
- PUT /api/vendors/{pk}/: Update a vendor
- DELETE /api/vendors/{pk}/: Delete a vendor

### Purchase Order API Endpoints

- POST /api/purchase_orders/: Create a new purchase order
- GET /api/purchase_orders/: List all purchase orders (filter by vendor with vendor query parameter)
- GET /api/purchase_orders/{pk}/: Retrieve a specific purchase order
- PUT /api/purchase_orders/{pk}/: Update a purchase order
- DELETE /api/purchase_orders/{pk}/: Delete a purchase order

### Vendor Performance API Endpoint
- GET /api/vendors/{pk}/performance/: Retrieve a vendor's performance metrics
Purchase Order Acknowledge API Endpoint
- POST /api/purchase_orders/{pk}/acknowledge/: Acknowledge a purchase order

# Example Usage

1. Create a New Vendor
    ```bash 
    curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Vendor 1",
    "contact_details": "vendor1@example.com",
    "address": "123 Vendor St.",
    "vendor_code": "VEND001"
    }' http://127.0.0.1:8000/api/vendors/

2. List All Vendors
    ```bash 
    curl -X GET http://127.0.0.1:8000/api/vendors/

3. Create a New Purchase Order
    ```bash 
    curl -X POST -H "Content-Type: application/json" -d '{
    "po_number": "PO001",
    "vendor": 1,
    "order_date": "2024-05-07T10:00:00Z",
    "delivery_date": "2024-05-14T10:00:00Z",
    "items": {"item1": 5, "item2": 10},
    "quantity": 15,
    "status": "pending",
    "issue_date": "2024-04-27T10:00:00Z"
    }' http://127.0.0.1:8000/api/purchase_orders/

4. Retrieve Vendor Performance Metrics
    ```bash 
    curl -X GET http://127.0.0.1:8000/api/vendors/1/performance/

# Admin Interface
Access the Django admin panel at http://127.0.0.1:8000/admin and use your superuser credentials to log in.

# Testing
Run the following command to execute the test suite and ensure everything is functioning correctly:
    ```bash 
    python manage.py test

# Code Structure
     
    vendor_management/
    ├── vendor_management/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── vendors/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── requirements.txt
    ├── db.sqlite3
    └── manage.py
