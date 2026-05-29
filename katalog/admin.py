from django.contrib import admin
from .models import Kategori, Produk

# Mengatur tampilan tabel di halaman Admin
@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'harga', 'stok', 'created_at') # Kolom yang muncul
    search_fields = ('nama', 'deskripsi') # Fitur pencarian
    list_filter = ('kategori',) # Fitur filter di samping kanan

admin.site.register(Kategori)

# Kustomisasi teks di halaman Admin
admin.site.site_header = "Panel Admin MyKatalog"
admin.site.site_title = "Admin MyKatalog"
admin.site.index_title = "Selamat Datang di Manajemen Katalog"