import requests

BASE_URL = "http://127.0.0.1:5000/products"

def add_product(name, description, price):
    product = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=product)
    if response.status_code == 201:
        print("Product added:", response.json())
    else:
        print("Error:", response.json())

def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        products = response.json()
        print("Products:", products)
    else:
        print("Error:", response.json())

# Example usage
add_product("Laptop", "A high-end laptop", 1500.00)
get_products()
