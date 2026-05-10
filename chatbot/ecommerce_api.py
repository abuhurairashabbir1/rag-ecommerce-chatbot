import requests

BASE_URL = "https://fakestoreapi.com"

def get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    response.raise_for_status()
    return response.json()

def get_product_by_id(product_id):
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    response.raise_for_status()
    return response.json()

def get_all_categories():
    response = requests.get(f"{BASE_URL}/products/categories")
    response.raise_for_status()
    return response.json()

def get_products_by_category(category):
    response = requests.get(f"{BASE_URL}/products/category/{category}")
    response.raise_for_status()
    return response.json()

def get_cleaned_products():
    products = get_all_products()
    cleaned = []
    for p in products:
        cleaned.append({
            "id":           p["id"],
            "title":        p["title"],
            "price":        p["price"],
            "description":  p["description"],
            "category":     p["category"],
            "rating":       p["rating"]["rate"],
            "rating_count": p["rating"]["count"],
            "image":        p["image"]
        })
    return cleaned
