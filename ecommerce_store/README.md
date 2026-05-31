# ShopAlpha — E-Commerce Store
### CodeAlpha Internship — Task 1

A full-stack e-commerce web application built with Django (Python).

## Features
- Product listings with category filtering
- Product detail pages
- Shopping cart (add, update, remove items)
- User registration & login
- Checkout with order placement
- Order history page
- Admin panel to manage products, categories, orders

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (built-in, no setup needed)

---

## Setup & Run Instructions (Windows)

### Step 1 — Install Django
Open Command Prompt and run:
```
pip install django pillow
```

### Step 2 — Navigate to the project folder
```
cd path\to\ecommerce_store
```
(Replace `path\to` with where you extracted the folder)

### Step 3 — Run migrations (sets up the database)
```
python manage.py migrate
```

### Step 4 — Create an admin account
```
python manage.py createsuperuser
```
Enter a username, email, and password when prompted.

### Step 5 — Add sample data (optional)
```
python manage.py loaddata
```

### Step 6 — Start the server
```
python manage.py runserver
```

### Step 7 — Open in browser
- **Website:** http://127.0.0.1:8000/
- **Admin panel:** http://127.0.0.1:8000/admin/

---

## Admin Login (pre-created)
- Username: `admin`
- Password: `admin123`

## How to Add Products
1. Go to http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Click "Categories" → Add category
4. Click "Products" → Add product

---

## GitHub Upload
Name your repo: `CodeAlpha_EcommerceStore`
