def test_get_authenticated_user(api_client, auth_token):

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = api_client.get(
        "/auth/me",
        headers=headers
    )

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["username"] == "emilys"