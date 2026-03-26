import requests
def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] ==1
def test_create_post():
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "hello", "body": "world", "userId": 1}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "hello"
def test_get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert len(response.json()) == 100