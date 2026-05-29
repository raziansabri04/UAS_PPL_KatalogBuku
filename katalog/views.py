from django.shortcuts import render, get_object_or_404
from .models import Buku # Pastikan ini 'Buku'

def index(request):
    # Mengambil semua data buku
    semua_buku = Buku.objects.all().order_by('-created_at')
    return render(request, 'katalog/index.html', {'daftar_buku': semua_buku})

def detail_produk(request, id):
    # Mengambil satu buku berdasarkan ID
    buku = get_object_or_404(Buku, id=id)
    return render(request, 'katalog/detail.html', {'p': buku})