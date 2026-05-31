from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produk/<int:id>/', views.detail_produk, name='detail_produk'),
    path('tentang/', views.tentang, name='tentang'), # Tambahkan ini
]