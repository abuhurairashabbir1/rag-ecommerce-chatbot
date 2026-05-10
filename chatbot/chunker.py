def chunk_products(products):
    chunks = []

    for product in products:
        pid   = product["id"]
        title = product["title"]
        price = product["price"]
        category    = product["category"]
        description = product["description"]
        rating      = product["rating"]
        count       = product["rating_count"]

        chunks.append({
            "text": f"{title} is priced at ${price}.",
            "product_id": pid,
            "product_title": title
        })

        chunks.append({
            "text": f"{title} belongs to the {category} category.",
            "product_id": pid,
            "product_title": title
        })

        chunks.append({
            "text": f"{title} description: {description}",
            "product_id": pid,
            "product_title": title
        })

        chunks.append({
            "text": f"{title} has a customer rating of {rating} out of 5 based on {count} reviews.",
            "product_id": pid,
            "product_title": title
        })

        chunks.append({
            "text": f"Product: {title} | Price: ${price} | Category: {category} | Rating: {rating}/5",
            "product_id": pid,
            "product_title": title
        })

    return chunks
