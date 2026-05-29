from django.shortcuts import render, get_object_or_404
from .models import Produk

# Fungsi untuk halaman utama (List semua produk)
def index(request):
    semua_produk = Produk.objects.all().order_by('-created_at')
    return render(request, 'katalog/index.html', {'daftar_produk': semua_produk})

# Fungsi untuk halaman detail (Melihat 1 produk saja)
def detail_produk(request, id):
    # Mengambil produk berdasarkan ID, jika tidak ada munculkan error 404
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'katalog/detail.html', {'p': produk})