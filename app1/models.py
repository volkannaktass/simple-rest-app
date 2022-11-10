from django.db import models

# Create your models here.
class Kitap(models.Model):
    baslik=models.CharField(max_length=70)

    def __str__(self):
        return self.baslik
    class Meta:
        verbose_name = 'Kitap'
        verbose_name_plural = 'Kitaplar'

class Yazar(models.Model):
    isim=models.CharField(max_length=30)
    soyisim=models.CharField(max_length=30)
    kitaplar=models.ManyToManyField(Kitap)
    
    def __str__(self):
        return '%s %s'%(self.isim,self.soyisim)
    class Meta:
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazarlar'



