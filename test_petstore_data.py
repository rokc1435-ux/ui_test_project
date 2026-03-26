import json
import pytest
import requests
with open('test_data.json', 'r',encoding = "utf-8") as f:
    load_data = json.load(f)
@pytest.mark.parametrize("pet",load_data)
def test_create_pet(pet):
    response = requests.post(
        "https://petstore.swagger.io/v2/pet",
        json=pet
    )
    assert response.status_code == 200
    assert response.json()["name"] == pet["name"]

