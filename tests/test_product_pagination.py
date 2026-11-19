def test_product_pagination(api_client):

    params = {
        "limit": 10,
        "skip": 0
    }

    response = api_client.get(
        "/products",
        params=params
    )

    assert response.status_code == 200

    response_data = response.json()

    assert len(response_data["products"]) == 10
    assert response_data["limit"] == 10
    assert response_data["skip"] == 0

    print("Here is the Total products:", response_data["total"])

def test_product_pagination_no_duplicates(api_client):

    response1 = api_client.get(
        "/products",
        params={"limit": 10, "skip": 0}
    )

    response2 = api_client.get(
        "/products",
        params={"limit": 10, "skip": 10}
    )

    assert response1.status_code == 200
    assert response2.status_code == 200

    products_page1 = response1.json()["products"]
    products_page2 = response2.json()["products"]

    ids_page1 = {product["id"] for product in products_page1}
    ids_page2 = {product["id"] for product in products_page2}

    assert ids_page1.isdisjoint(ids_page2) #Here, we're checking that the first and second pages don't contain duplicate product IDs.