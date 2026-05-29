from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100) # Misal: Fiksi, Sains, Sejarah

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori Buku"

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100) # Tambahan khusus buku
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    sinopsis = models.TextField() # Sebelumnya deskripsi
    harga = models.PositiveIntegerField()
    stok = models.IntegerField(default=0)
    sampul = models.ImageField(upload_to='buku/', null=True, blank=True) # Sebelumnya gambar
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "Daftar Buku"