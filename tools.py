import json
from logging_config import log

with open("product.json") as file:
    products = json.load(file)

def search_product(query):
    log.info("tool call: search_product({query!r})") # activate repr() by !r
    query = query.lower().strip()
    found = [p for p in products if query in p["name"].lower() or query in p["description"].lower()]

    if not found:
        return f"No product found for '{query}'"
    return "\n".join(f"{p['id']}: {p['name']} - {p['description']} - {p['price']:,} RWF" for p in found)

def check_price(product_id):
    log.info(f"tool call: check_price({product_id!r})")
    product_id = str(product_id).strip().upper()

    for p in products:
        if p["id"] == product_id:
            return f"{p['name']} ({p['id']}) costs {p['price']:,} RWF."

    log.warning(f"tool failure: product {product_id} not found")
    return f"Product {product_id} not found. No price available."