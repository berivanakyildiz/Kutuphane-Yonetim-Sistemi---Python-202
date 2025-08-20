import pytest
from library import Library, Book

# ==== Temel İşlevler ====

def test_add_and_remove_book(tmp_path):
    # Geçici dosya ile test
    file = tmp_path / "library.json"
    lib = Library(filename=str(file))

    # Başlangıçta boş olmalı
    assert lib.list_books() == []

    # Manuel kitap ekle
    book = Book("Test Title", "Test Author", "12345")
    lib.books.append(book)
    lib.save_books()

    # Dosyadan tekrar yükle
    lib2 = Library(filename=str(file))
    assert lib2.find_book("12345") is not None

    # Silme testi
    assert lib2.remove_book("12345") is True
    assert lib2.find_book("12345") is None


# ==== OpenLibrary API'yi taklit ederek test ====

class FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload or {}

    def json(self):
        return self._payload


def test_add_book_from_api_success(monkeypatch, tmp_path):
    file = tmp_path / "library.json"
    lib = Library(filename=str(file))

    # httpx.get'i sahteleyelim
    def fake_get(url, **kwargs):
        if "isbn" in url:
            return FakeResponse(200, {
                "title": "Fake Title",
                "authors": [{"key": "/authors/OL12345A"}]
            })
        if "/authors/" in url:
            return FakeResponse(200, {"name": "Fake Author"})
        return FakeResponse(404, {})

    import httpx
    monkeypatch.setattr(httpx, "get", fake_get)

    # Ekleme başarılı olmalı
    book = lib.add_book_from_api("99999")
    assert book is not None
    assert book.title == "Fake Title"
    assert "Fake Author" in book.author


def test_add_book_from_api_not_found(monkeypatch, tmp_path):
    file = tmp_path / "library.json"
    lib = Library(filename=str(file))

    def fake_get(url, **kwargs):
        return FakeResponse(404, {})

    import httpx
    monkeypatch.setattr(httpx, "get", fake_get)

    # Kitap bulunamadığı için None dönmeli
    book = lib.add_book_from_api("00000")
    assert book is None
