import os
import django
from django.conf import settings
from django.urls import path
from django.shortcuts import render, redirect
from django.core.management import execute_from_command_line
from django.db import models
from django.contrib import admin

from django.urls import path, include

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="abc123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],

    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "shop",
    ],

    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ],

    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },

   
    CSRF_TRUSTED_ORIGINS=[
        "https://redapple-egop.onrender.com/",
        "http://localhost:8000",
    ],

    TEMPLATES=[{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }],

    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
    STATIC_URL="/static/",

    # ✅ Add login redirects to fix login/logout
    LOGIN_URL="/accounts/login/",
    LOGIN_REDIRECT_URL="/",
    LOGOUT_REDIRECT_URL="/",
)


django.setup()

from shop.models import Product, Order
from django.contrib.auth.models import User  # <-- Add this

# --- CREATE SUPERUSER HERE ---
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123"
    )
    print("Superuser created: username='admin', password='admin123'")

from shop.models import Product, Order


# --- Views ---
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def about(request):
    return render(request, "about.html")

def products_view(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def buy(request, product_id):
    product = Product.objects.get(id=product_id)
    Order.objects.create(product=product)
    return redirect("/orders/")

def orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

# --- URLs ---
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("shop.urls")),  # include shop app URLs
    # Add this to enable login/logout pages
    
]




# --- Run Server ---
if __name__ == "__main__":
    from django.core.management import call_command

    call_command("makemigrations", "shop", interactive=False)
    call_command("migrate", interactive=False)




    # Seed products
   # Seed 20 products safely
products_to_add = [
    {"name": "Pizza", "price": 12.99, "description": "Delicious cheese pizza", "image": "https://images.pexels.com/photos/4109085/pexels-photo-4109085.jpeg"},
    {"name": "Burger", "price": 8.99, "description": "Juicy beef burger", "image": "https://images.pexels.com/photos/1639562/pexels-photo-1639562.jpeg"},
    {"name": "Pasta", "price": 10.99, "description": "Italian pasta with sauce", "image": "https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg"},
    {"name": "Sushi", "price": 15.99, "description": "Fresh sushi platter", "image": "https://images.pexels.com/photos/357756/pexels-photo-357756.jpeg"},
    {"name": "Salad", "price": 7.99, "description": "Healthy vegetable salad", "image": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"},
    {"name": "Steak", "price": 18.99, "description": "Grilled ribeye steak", "image": "https://images.pexels.com/photos/675951/pexels-photo-675951.jpeg"},
    {"name": "Ice Cream", "price": 5.99, "description": "Vanilla ice cream scoop", "image": "https://d3s8tbcesxr4jm.cloudfront.net/recipe-images/v0/homemade-cherry-ice-cream_large.jpg"},
    {"name": "Sandwich", "price": 6.99, "description": "Fresh sandwich with veggies", "image": "https://images.pexels.com/photos/1600714/pexels-photo-1600714.jpeg"},
    {"name": "Donut", "price": 2.99, "description": "Glazed donut", "image": "https://images.pexels.com/photos/533325/pexels-photo-533325.jpeg"},
    {"name": "Soup", "price": 4.99, "description": "Hot vegetable soup", "image": "https://images.pexels.com/photos/1640772/pexels-photo-1640772.jpeg"},
    {"name": "Fries", "price": 3.99, "description": "Crispy french fries", "image": "https://images.pexels.com/photos/1583884/pexels-photo-1583884.jpeg"},
    {"name": "Cake", "price": 9.99, "description": "Chocolate cake slice", "image": "https://images.pexels.com/photos/3026805/pexels-photo-3026805.jpeg"},
    {"name": "Taco", "price": 7.49, "description": "Spicy beef taco", "image": "https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg"},
    {"name": "Chocolate", "price": 4.49, "description": "Milk chocolate bar", "image": "https://images.pexels.com/photos/302489/pexels-photo-302489.jpeg"},
    {"name": "Pancakes", "price": 6.99, "description": "Fluffy pancakes with syrup", "image": "https://images.pexels.com/photos/376464/pexels-photo-376464.jpeg"},
    {"name": "Bagel", "price": 3.49, "description": "Fresh baked bagel", "image": "https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg"},
    {"name": "Chicken Wings", "price": 11.99, "description": "Spicy chicken wings", "image": "https://images.pexels.com/photos/616401/pexels-photo-616401.jpeg"},
    {"name": "Cheese Toast", "price": 5.49, "description": "Golden cheese toast", "image": "https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg"},
    {"name": "Smoothie", "price": 4.99, "description": "Mixed fruit smoothie", "image": "https://images.pexels.com/photos/373948/pexels-photo-373948.jpeg"},
    {"name": "Cupcake", "price": 3.99, "description": "Vanilla cupcake with frosting", "image": "https://handletheheat.com/wp-content/uploads/2016/02/best-chocolate-cupcakes-recipe-SQUARE.jpg"},
]





for p in products_to_add:
    Product.objects.get_or_create(name=p["name"], defaults=p)


execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])

