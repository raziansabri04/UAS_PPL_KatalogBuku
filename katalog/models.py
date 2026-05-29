from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Kategori"

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    deskripsi = models.TextField()
    harga = models.PositiveIntegerField()
    stok = models.IntegerField(default=0)
    gambar = models.ImageField(upload_to='produk/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Produk"