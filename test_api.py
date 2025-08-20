from fastapi.testclient import TestClient
from api import app, library
from library import Book

client = TestClient(app)

def test_get_books_empty():
    library.books = []  # Temizle
    resp = client.get("/books")
    assert resp.status_code == 200
    assert resp.json() == []


def test_add_book_endpoint(monkeypatch):
    # Sahte add_book_from_api
    def fake_add(isbn: str):
        return Book("Mock Book", "Mock Author", isbn)

    monkeypatch.setattr(library, "add_book_from_api", fake_add)

    resp = client.post("/books", json={"isbn": "12345"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Mock Book"
    assert data["author"] == "Mock Author"
    assert data["isbn"] == "12345"


def test_add_book_not_found(monkeypatch):
    monkeypatch.setattr(library, "add_book_from_api", lambda isbn: None)

    resp = client.post("/books", json={"isbn": "99999"})
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Kitap bulunamadı"


def test_delete_book(monkeypatch):
    monkeypatch.setattr(library, "remove_book", lambda isbn: True)

    resp = client.delete("/books/11111")
    assert resp.status_code == 200
    assert "silindi" in resp.json()["message"]


def test_delete_book_not_found(monkeypatch):
    monkeypatch.setattr(library, "remove_book", lambda isbn: False)

    resp = client.delete("/books/22222")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Kitap bulunamadı"
