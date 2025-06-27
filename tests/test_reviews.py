def test_add_review_to_book(client):
    # First create a book
    book = client.post("/books", json={"title": "The Hobbit", "author": "Tolkien"}).json()
    book_id = book["id"]

    # Then add review
    review_data = {"comment": "Amazing read", "rating": 5}
    response = client.post(f"/books/{book_id}/reviews", json=review_data)

    assert response.status_code == 201
    review = response.json()
    assert review["comment"] == "Amazing read"
    assert review["rating"] == 5
    assert review["book_id"] == book_id

def test_get_reviews_for_book(client):
    book = client.post("/books", json={"title": "Dune", "author": "Herbert"}).json()
    book_id = book["id"]
    client.post(f"/books/{book_id}/reviews", json={"comment": "Epic!", "rating": 4})

    response = client.get(f"/books/{book_id}/reviews")
    assert response.status_code == 200
    reviews = response.json()
    assert isinstance(reviews, list)
    assert len(reviews) >= 1
