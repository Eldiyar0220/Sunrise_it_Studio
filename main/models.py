from datetime import datetime

from django.db import models

# Create your models here.
from account.models import User


class Country(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField()


    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'pk': self.pk})



class Image(models.Model):
    image = models.ImageField(upload_to='posts')
    recipe = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url


#NEWS

#товар
class Parcels(models.Model):
    order = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    date = models.DateField(blank=False, default=datetime.now().strftime("%d.%m.%Y"))
    recipient = models.CharField(null = False, max_length = 100)
    parcels_name = models.CharField(null = False, max_length = 100)
    amount = models.PositiveIntegerField(null = True)
    price = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    weight = models.DecimalField(default = 0.00, max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100, verbose_name=u"Страна")
    treck = models.CharField(max_length=50, null=False, unique=True, default=False)
    status = models.BooleanField(default = False)
    category = models.CharField(max_length=100,null=False,default=False)
    web_site = models.URLField(max_length=200,null=False,default=False)
    comment = models.TextField(max_length=324,null=True)


#Sklad
class CountrySklad(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.slug

class Sklad(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    CountrySklad = models.ForeignKey(CountrySklad, on_delete=models.CASCADE, related_name='sklads')
    created = models.DateTimeField()


    def __str__(self):
        return self.title

    @property
    def get_image(self):
        return self.images.first()



class Images(models.Model):
    image = models.ImageField(upload_to='sklads')
    recipe = models.ForeignKey(Sklad, on_delete=models.CASCADE, related_name='sklads')

    def __str__(self):
        return self.image.url