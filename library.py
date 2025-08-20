import json
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([vars(book) for book in self.books], f, indent=2, ensure_ascii=False)

    def list_books(self):
        return self.books

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn: str):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def add_book_from_api(self, isbn: str):
        """Fetch book info from Open Library API and add to library"""
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, timeout=10.0, follow_redirects=True)
            print("DEBUG - Status code:", response.status_code)
            if response.status_code == 200:
                data = response.json()
                print("DEBUG - Data:", data)
                title = data.get("title", "Unknown Title")
                authors = []

                # author bilgilerini al
                if "authors" in data:
                    for author_ref in data["authors"]:
                        author_key = author_ref.get("key")
                        if author_key:
                            author_url = f"https://openlibrary.org{author_key}.json"
                            try:
                                author_resp = httpx.get(author_url, timeout=10.0)
                                if author_resp.status_code == 200:
                                    author_data = author_resp.json()
                                    authors.append(author_data.get("name", "Unknown"))
                            except httpx.RequestError:
                                pass

                author_str = ", ".join(authors) if authors else "Unknown"

                book = Book(title=title, author=author_str, isbn=isbn)
                self.books.append(book)
                self.save_books()
                return book
            elif response.status_code == 404:
                return None
        except httpx.RequestError:
            return None
