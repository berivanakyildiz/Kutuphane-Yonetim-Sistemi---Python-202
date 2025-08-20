from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library

app = FastAPI(title="Library API", description="Kütüphane Yönetim Sistemi", version="1.0")

library = Library()

class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str

class BookRequest(BaseModel):
    isbn: str

@app.get("/books", response_model=list[BookResponse])
def get_books():
    return [vars(b) for b in library.list_books()]

@app.post("/books", response_model=BookResponse)
def add_book(request: BookRequest):
    book = library.add_book_from_api(request.isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    return vars(book)

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if library.remove_book(isbn):
        return {"message": f"{isbn} silindi."}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")
