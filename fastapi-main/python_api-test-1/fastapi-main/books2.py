from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'One Piece', 'Eiichiro Oda', 'A great book!', 5),
    Book(2, 'Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'A magical journey!', 5),
    Book(3, 'The Hobbit', 'J.R.R. Tolkien', 'An epic adventure!', 5),
    Book(4, '1984', 'George Orwell', 'A chilling dystopia!', 4.5),
    Book(5, 'To Kill a Mockingbird', 'Harper Lee', 'A powerful story of justice!', 5),
    Book(6, 'The Great Gatsby', 'F. Scott Fitzgerald', 'A classic tale of the American Dream!', 4),
    Book(7, 'Pride and Prejudice', 'Jane Austen', 'A timeless romance!', 5)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.post("/create-book")
# async def create_book(book_request=Body()):
#     BOOKS.append(book_request)

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=5)


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
