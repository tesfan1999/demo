from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

books_db = []

class Book(BaseModel):
    title: str
    author: str
    pages: int
    read: Optional[bool] = False

@app.post("/books/")
async def create_book(book: Book):
    books_db.append(book.dict())
    return book

@app.get("/books/")
async def read_books():
    return books_db

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    books_db[book_id] = book.dict()
    return {"message": "Book updated successfully"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    books_db.pop(book_id)
    return {"message": "Book deleted successfully"}
#run with 'uvicorn name of pythonfile:app --reload'
#use Post man to run the methods