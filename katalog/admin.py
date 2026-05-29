from django.contrib import admin
from .models import Kategori, Buku # Pastikan ini 'Buku', bukan 'Produk'

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    # Sesuaikan list_display dengan nama field baru di model Buku
    list_display = ('judul', 'penulis', 'harga', 'stok', 'kategori') 
    search_fields = ('judul', 'penulis')
    list_filter = ('kategori',)

admin.site.register(Kategori)

# Opsional: Kustomisasi judul dashboard
admin.site.site_header = "Panel Admin Katalog Buku"
admin.site.index_title = "Manajemen Koleksi Buku"