def test_create_book(client):
    response = client.post("/books", json={"title": "1984", "author": "George Orwell"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "1984"
    assert data["author"] == "George Orwell"
    assert "id" in data

def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) > 0
