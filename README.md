# 📚 BookArchive - Aplikasi Manajemen Katalog Buku

**Identitas Mahasiswa:**
- **Nama:** Razian Sabri
- **NIM:** 2308107010050
- **Mata Kuliah:** Praktikum Proyek Perangkat Lunak

---

## 📝 Deskripsi Proyek
**BookArchive** adalah aplikasi web berbasis Django yang dirancang untuk mengelola koleksi buku secara digital. Aplikasi ini memungkinkan pengguna umum untuk melihat daftar buku yang tersedia dengan fitur pencarian dan filter modern, sementara administrator dapat mengelola database buku melalui dashboard khusus yang aman dengan sistem CRUD lengkap.

## 🧰 Teknologi yang Digunakan
- **Framework:** Django 6.x (Python Framework)
- **Backend:** Python 3.13+
- **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Database:** SQLite
- **Manajemen Gambar:** Pillow Library

## ✨ Fitur Utama
- **Halaman Bagian User (Public):**
    - **Landing Page:** Tampilan katalog buku menggunakan sistem Grid dan Card yang simetris.
    - **Real-time Search:** Fitur pencarian buku berdasarkan judul atau penulis tanpa reload halaman.
    - **Category Filtering:** Filter buku berdasarkan kategori menggunakan dropdown menu yang dinamis.
    - **Halaman Detail:** Informasi lengkap buku (Sinopsis, Harga, Stok) dan simulasi pembelian via modal.
    - **Halaman Informasi:** Halaman "Tentang Kami" yang menjelaskan profil aplikasi dan pengembang.
    - **UI/UX Improvements:** Animasi Fade-in saat halaman dimuat dan tombol *Back to Top* untuk navigasi cepat.
- **Dashboard Admin (Private):**
    - **Autentikasi:** Sistem login aman untuk mengelola data.
    - **CRUD Kategori:** Manajemen kategori buku (Fiksi, Teknologi, Sains, dll).
    - **CRUD Buku:** Manajemen data buku lengkap termasuk fitur upload sampul buku.
    - **Admin Preview:** Tampilan thumbnail sampul buku langsung di tabel daftar buku admin.

## ⚙️ Panduan Instalasi

1. **Clone Repository**
   ```bash
   git clone https://github.com/raziansabri04/UAS_PPL_KatalogBuku
   cd UAS_PPL_KATALOG

    Setup Virtual Environment
    code Bash

    python -m venv venv
    # Aktivasi (Windows):
    venv\Scripts\activate
    # Aktivasi (Mac/Linux):
    source venv/bin/activate

    Install Dependensi
    code Bash

    pip install -r requirements.txt

    Persiapan Database & Import Data
    code Bash

    python manage.py migrate
    # Import data contoh (20 buku & 5 kategori)
    python manage.py loaddata data_buku.json

    Menjalankan Aplikasi
    code Bash

    python manage.py runserver

    Akses aplikasi di: http://127.0.0.1:8000/

👤 Akun Admin (Demo)

    URL: http://127.0.0.1:8000/admin

    Username: razian

    Password: razian123 

📦 Output Tugas

    Link Repository: https://github.com/raziansabri04/UAS_PPL_KatalogBuku

    Link Video Presentasi: [Youtube/Google Drive Link]