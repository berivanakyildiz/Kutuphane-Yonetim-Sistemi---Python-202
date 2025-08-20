from library import Library

def main():
    library = Library()

    while True:
        print("\n=== Kütüphane Menüsü ===")
        print("1. Kitap Ekle (ISBN ile)")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            isbn = input("ISBN girin: ")
            book = library.add_book_from_api(isbn)
            if book:
                print(f"Kitap eklendi: {book}")
            else:
                print("Kitap bulunamadı veya eklenemedi.")

        elif choice == "2":
            isbn = input("Silmek istediğiniz kitabın ISBN'ini girin: ")
            if library.remove_book(isbn):
                print("Kitap silindi.")
            else:
                print("Kitap bulunamadı.")

        elif choice == "3":
            books = library.list_books()
            if books:
                print("\n--- Kütüphanedeki Kitaplar ---")
                for b in books:
                    print(b)
            else:
                print("Kütüphanede hiç kitap yok.")

        elif choice == "4":
            isbn = input("Aramak istediğiniz kitabın ISBN'ini girin: ")
            book = library.find_book(isbn)
            if book:
                print(f"Bulunan kitap: {book}")
            else:
                print("Kitap bulunamadı.")

        elif choice == "5":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
