import requests

def test_create_pet():
    response = requests.post(
        "https://petstore.swagger.io/v2/pet",
        json={"id": 123, "name": "doggie", "status": "available"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "doggie"
def test_get_pet():
    response = requests.get(
        "https://petstore.swagger.io/v2/pet/123"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "doggie"
def test_update_pet():
    response = requests.put(
        "https://petstore.swagger.io/v2/pet",
        json={"id": 123, "name": "kitty", "status": "available"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "kitty"
def test_delete_pet():
    response = requests.delete(
        "https://petstore.swagger.io/v2/pet/123"
    )
    assert response.status_code == 200