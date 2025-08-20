"# GlobalAIBootcamp Projesi" 
# 📚 Python 202 Bootcamp - Kütüphane Yönetim Sistemi

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir **Kütüphane Yönetim Sistemi** uygulamasıdır.  
Proje, üç aşamadan oluşmaktadır:

1. **Nesne Yönelimli Programlama (OOP)** ile temel kütüphane uygulaması  
2. **API entegrasyonu (Open Library API)** ile ISBN üzerinden kitap ekleme  
3. **FastAPI** ile REST API geliştirme  

---

## 🚀 Özellikler

- Kitap ekleme, silme, arama ve listeleme (OOP mantığıyla)
- `library.json` dosyasında kalıcı veri saklama
- Open Library API’den ISBN ile kitap bilgilerini otomatik çekme
- FastAPI ile REST API üzerinden kitap yönetimi
- Pytest ile birim testleri

---

## 📂 Proje Yapısı

```bash
.
├── book.py              # Book sınıfı
├── library.py           # Library sınıfı (kitap yönetimi + API entegrasyonu)
├── main.py              # Terminal arayüzü
├── api.py               # FastAPI REST API
├── tests/
├── test_library.py  # Library sınıfı testleri
└── test_api.py      # FastAPI endpoint testleri
├── requirements.txt     # Gerekli bağımlılıklar
└── README.md            # Bu dosya

KURULUM
1- Depoyu klonlayın
  git clone https://github.com/<kullanici-adi>/<repo-adi>.git
  cd <repo-adi>

2- Sanal ortam oluşturun
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows

3- Gerekli kütüphaneleri yükleyin
  pip install -r requirements.txt
       requirements.txt dosyasında şunlar vardır:
        -fastapi
        -uvicorn
        -httpx
        -pytest

KULLANIM
1- Terminal Uygulaması
    python main.py
 --> Çalıştırıldığında menü açılır:
       === Kütüphane Menüsü ===
          1. Kitap Ekle (ISBN ile)
          2. Kitap Sil
          3. Kitapları Listele
          4. Kitap Ara
          5. Çıkış

2- FastAPI REST API
   uvicorn api:app --reload
--> Tarayıcıda aç: http://127.0.0.1:8000/docs  (cmd ekranında da görebilirsiniz)

Buradan şu endpointleri kullanabilirsin:
    -GET /books → Tüm kitapları listeler
    -POST /books → ISBN ile kitap ekler
    -DELETE /books/{isbn} → Kitap siler

TESTLER
Tüm testleri çalıştırmak için:
    pytest -v
