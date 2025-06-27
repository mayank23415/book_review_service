import time
from app.services.cache import r

def test_books_cache_integration(client):
    r.delete("books")  # Ensure cache is empty before test
    assert r.get("books") is None  # Cache miss

    # Trigger API call to fetch from DB and populate cache
    response = client.get("/books")
    assert response.status_code == 200

    # Cache should now be populated
    cached = r.get("books")
    assert cached is not None
