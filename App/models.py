from django.db import models

class Inventory(models.Model) :
    
    UKURAN = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        )
    
    JENIS = (
        ('Vans', 'Vans'),
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Puma', 'Puma'),
        ('Hushpuppies', 'Hushpuppies'),
        ('Kenzo', 'Kenzo'),
        ('Converse', 'Converse'),
        ('Reebok', 'Reebok'),
        ('Reebok', 'Reebok'),
        ('Jordan', 'Jordan'),
        ('Stussy', 'Stussy'),
        ('Volcom', 'Volcom'),
        ('New Balance', 'New Balance'),
        ('Thrasher', 'Thrasher'),
        ('Champion', 'Champion'),
        )
    
    no_barang = models.IntegerField(primary_key=True)
    nama_barang = models.CharField(max_length=100)
    no_sku = models.CharField(max_length=20)
    ukuran = models.CharField(max_length=2, null=True,choices=UKURAN)
    jumlah_barang = models.IntegerField(null=True)
    Jenis_barang = models.CharField(max_length=25, null=True,choices=JENIS)
    
    def __str__(self) -> str:
        return self.nama_barang
    

    #JSON
    def get_data(self):
        return{
            'no_barang': self.no_barang,
            'nama_barang': self.nama_barang,
            'no_sku': self.no_sku,
            'ukuran': self.ukuran,
            'jumlah_barang': self.jumlah_barang,
            'Jenis_barang': self.Jenis_barang,
        }