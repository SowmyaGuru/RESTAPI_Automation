def test_get_all_products(api_client):

    response = api_client.get("/products")

    assert response.status_code == 200

    response_data = response.json()

    assert "products" in response_data
    assert len(response_data["products"]) > 0
    assert response_data["total"] > 0

    # Validate individual product details
    for product in response_data["products"]:

        assert "id" in product
        assert "title" in product
        assert "price" in product

        assert isinstance(product["id"], int)
        assert isinstance(product["title"], str)
        assert isinstance(product["price"], (int, float))
        assert product["price"] > 0