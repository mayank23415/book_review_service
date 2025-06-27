# Book Review Service

A simple Book Review backend built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Redis**. It provides a clean API to manage books and reviews, with caching and automated testing.

---

## Features

- ✅ RESTful endpoints using FastAPI  
- ✅ PostgreSQL as the main data store  
- ✅ Redis caching for book listings  
- ✅ SQLAlchemy ORM with Alembic migrations  
- ✅ Pytest-based unit and integration tests  
- ✅ OpenAPI documentation out of the box  

---

## Endpoints

| Method | Route                    | Description                     |
|--------|--------------------------|---------------------------------|
| GET    | `/books`                 | Get all books (cached)          |
| POST   | `/books`                 | Add a new book                  |
| GET    | `/books/{id}/reviews`    | Get reviews for a specific book |
| POST   | `/books/{id}/reviews`    | Add a review for a book         |

---

## Project Structure

```
book_review_service/
├── app/
│   ├── db/         # Database setup and session
│   ├── models/     # SQLAlchemy models
│   ├── routers/    # API route handlers
│   ├── schemas/    # Pydantic request/response models
│   ├── services/   # Redis cache logic
│   └── main.py     # FastAPI app entrypoint
├── alembic/        # Alembic migration scripts
├── tests/          # Unit and integration tests
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql://user:password@localhost:5432/bookdb
REDIS_URL=redis://localhost:6379
```

Make sure both PostgreSQL and Redis are running.

### 3. Run migrations

```bash
alembic upgrade head
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

- OpenAPI Docs: [http://localhost:8000/docs](http://localhost:8000/docs)  
- Redoc Docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## Running Tests

```bash
pytest
```

Test coverage includes:

- Unit tests for books and reviews endpoints
- Integration test covering cache-miss path for Redis

---

## Design Notes

- The `GET /books` endpoint first tries to return results from Redis. If not found, it fetches from the database and caches the result.
- Indexing is added on the `reviews.book_id` column to optimize lookups.
- Error handling is added to gracefully fall back when Redis is unavailable.
- The project is structured to be modular and easily extensible.

---

## Possible Improvements

- Add authentication and authorization (e.g., JWT)
- Add pagination and search support
- Extend with GraphQL and real-time subscriptions (e.g., using WebSockets)
- Dockerize the application for container-based deployment

---

## Author

**Mayank Awasthi**  
Email: mayank23415@example.com  
GitHub: [github.com/mayank23415](https://github.com/mayank23415)

---

## License

This project is licensed under the MIT License.
