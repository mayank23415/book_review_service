from app.db.database import Base, engine
from app.models.book import Book
from app.models.review import Review

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
