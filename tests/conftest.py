import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "postgresql://user:password@localhost:5432/bookdb"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def client():
    # Drop and recreate tables before running tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Dependency override to use the test DB session
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # Apply override
    app.dependency_overrides[get_db] = override_get_db

    # Provide a test client to the tests
    yield TestClient(app)
