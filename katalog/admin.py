from django.contrib import admin
from django.utils.html import format_html
from .models import Kategori, Buku

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    # Menambahkan 'show_sampul' di daftar kolom
    list_display = ('show_sampul', 'judul', 'penulis', 'kategori', 'harga', 'stok')
    list_filter = ('kategori',)
    search_fields = ('judul', 'penulis')

    # Fungsi untuk menampilkan foto kecil
    def show_sampul(self, obj):
        if obj.sampul:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.sampul.url)
        return "No Image"
    
    show_sampul.short_description = 'Sampul'

admin.site.register(Kategori)