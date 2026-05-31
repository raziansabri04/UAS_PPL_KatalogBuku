from django.shortcuts import render, get_object_or_404
from .models import Buku, Kategori

# Fungsi untuk Halaman Utama (dengan Filter Kategori)
def index(request):
    semua_buku = Buku.objects.all().order_by('-created_at')
    semua_kategori = Kategori.objects.all()
    context = {
        'daftar_buku': semua_buku,
        'daftar_kategori': semua_kategori,
    }
    return render(request, 'katalog/index.html', context)

# Fungsi untuk Halaman Detail Buku (INI YANG TADI HILANG/ERROR)
def detail_produk(request, id):
    # Mengambil buku berdasarkan ID, jika tidak ada kirim error 404
    buku = get_object_or_404(Buku, id=id)
    return render(request, 'katalog/detail.html', {'p': buku})