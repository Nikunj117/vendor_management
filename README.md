# Vendor Management System

## Overview
This is a Vendor Management System built using Django and Django REST Framework. It manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features
- **Vendor Profile Management**
- **Purchase Order Tracking**
- **Vendor Performance Evaluation**

### Core Features
1. Vendor Profile Management
2. Purchase Order Tracking
3. Vendor Performance Evaluation

## Installation

### Clone Repository
```bash
git clone <REPO_URL>
cd <REPO_DIRECTORY>

README.md file with instructions.

md
Copy code
# Vendor Management System

## Overview
This is a Vendor Management System built using Django and Django REST Framework. It manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Features
- **Vendor Profile Management**
- **Purchase Order Tracking**
- **Vendor Performance Evaluation**

### Core Features
1. Vendor Profile Management
2. Purchase Order Tracking
3. Vendor Performance Evaluation

## Installation

### Clone Repository
```bash
git clone <REPO_URL>
cd <REPO_DIRECTORY>
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Database Setup
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create Superuser
bash
Copy code
python manage.py createsuperuser
Start Server
bash
Copy code
python manage.py runserver
Usage
API Endpoints
Vendor API Endpoints
POST /api/vendors/: Create a new vendor
GET /api/vendors/: List all vendors
GET /api/vendors/{vendor_id}/: Retrieve a specific vendor
PUT /api/vendors/{vendor_id}/: Update a vendor
DELETE /api/vendors/{vendor_id}/: Delete a vendor
Purchase Order API Endpoints
POST /api/purchase_orders/: Create a new purchase order
GET /api/purchase_orders/: List all purchase orders (filter by vendor with vendor query parameter)
GET /api/purchase_orders/{po_id}/: Retrieve a specific purchase order
PUT /api/purchase_orders/{po_id}/: Update a purchase order
DELETE /api/purchase_orders/{po_id}/: Delete a purchase order
Vendor Performance API Endpoint
GET /api/vendors/{vendor_id}/performance/: Retrieve a vendor's performance metrics
Purchase Order Acknowledge API Endpoint
POST /api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order
Testing
bash
Copy code
python manage.py test
Note: Replace <REPO_URL> and <REPO_DIRECTORY> with the actual values.






