from django.contrib import admin
from App.models import Inventory

class InventoryAdmin(admin.ModelAdmin) :
    list_display = ['no_barang','nama_barang', 'no_sku', 'ukuran', 'jumlah_barang', 'Jenis_barang']
    list_per_page = 8
    search_fields = ['nama_barang','no_sku',]
    
admin.site.register(Inventory, InventoryAdmin)