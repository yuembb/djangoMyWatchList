from django.db import models
from django.contrib.auth.models import User #* burda djangonun oluşturduğu user model ini dahil ediyoruz projemize
from django.utils.text import slugify #* türkçe karakterleri ve boşlukları okunucak hale dönüştürüyor


# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50 )
    
    def __str__(self):
        return self.title
    
class Type(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Tür"), max_length=50 )
    
    def __str__(self):
        return self.title
    
class Dramatype(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Tür"), max_length=50 )
    
    def __str__(self):
        return self.title
    
class Animetype(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Tür"), max_length=50 )
    
    def __str__(self):
        return self.title

class Movietype(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Tür"), max_length=50 )
    
    def __str__(self):
        return self.title

class Gametype(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    title = models.CharField(("Tür"), max_length=50 )
    
    def __str__(self):
        return self.title


class Card(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    type = models.ForeignKey(Type, verbose_name=("Tür"), on_delete=models.CASCADE , null=True)
    title = models.CharField(("Başlık"), max_length=100)
    text = models.TextField(("İçerik"))
    date_now = models.DateField(("Tarih - Saat"), auto_now_add=True)
    author = models.CharField(("Kullanıcı"), max_length=50)    
    image = models.ImageField(("Resim"), upload_to='cards', max_length=200)

    def __str__(self):
        return self.title
    




class Comment(models.Model):

    card = models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE)
    fname = models.CharField(("İsim"), max_length=50)
    text = models.TextField(("Yorum"))
    date_now = models.DateField(("Tarih - Saat") , auto_now_add=False)

    def __str__(self):
        return self.fname
    
    
    
class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı Adı"), on_delete=models.CASCADE)
   address = models.CharField(("Adres"), max_length=100, blank=True, default="-")
   tel = models.CharField(("Telefon numarası"), max_length=10, default="-")
   job = models.CharField(("Meslek"), max_length=40, blank=True, default="-")
   image = models.ImageField(("Profil Resmi"), upload_to='profile', max_length=255, blank=True, null=True)
   password = models.CharField(("Şifre"), max_length=50)
   slug = models.SlugField(("Slug"), null=True , blank=True)

   def __str__(self):
      return self.user.username
   
   def save(self, *args, **kwargs):

      self.slug = slugify(self.name)
      self.tel = self.tel[:10]
      self.job = self.job[:40]
      self.address = self.address[:100]
      super(Profile, self).save(*args, **kwargs)




