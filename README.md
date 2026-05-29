# 📚 BookArchive - Aplikasi Manajemen Katalog Buku

Tugas Mata Kuliah: **Praktikum Proyek Perangkat Lunak**  
Deadline: **Minggu, 31 Mei 2026 pukul 23.59 WIB**

---

## 📝 Deskripsi Proyek
**BookArchive** adalah aplikasi web berbasis Django yang dirancang untuk mengelola koleksi buku secara digital. Aplikasi ini memungkinkan pengguna umum untuk melihat daftar buku yang tersedia, sementara administrator dapat mengelola database buku melalui dashboard khusus yang aman.

## 🧰 Teknologi yang Digunakan
- **Framework:** Django (Python) - Memanfaatkan fitur Django Admin untuk Dashboard.
- **Backend:** Python 3.x
- **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive Design)
- **Database:** SQLite
- **Handling Gambar:** Pillow library untuk manajemen upload sampul buku.

## ✨ Fitur Utama
- **Halaman Bagian User (Public):**
    - **Landing Page:** Menampilkan daftar semua koleksi buku dalam bentuk Card.
    - **Detail Buku:** Informasi lengkap mengenai judul, penulis, sinopsis, dan harga buku.
    - **Responsive UI:** Tampilan tetap rapi di perangkat mobile maupun desktop.
- **Dashboard Admin (Private):**
    - **Autentikasi:** Hanya admin terdaftar yang dapat masuk.
    - **Manajemen Kategori:** CRUD (Create, Read, Update, Delete) kategori buku (seperti Fiksi, Edukasi, dll).
    - **Manajemen Buku:** CRUD lengkap untuk data buku termasuk upload sampul buku.

## ⚙️ Panduan Instalasi

1. **Clone Repository**
   ```bash
   git clone <link-repo-github-kamu>
   cd katalog_buku