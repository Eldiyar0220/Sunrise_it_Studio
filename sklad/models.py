from django.db import models

# Create your models here.
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



class Image(models.Model):
    image = models.ImageField(upload_to='sklads')
    recipe = models.ForeignKey(Sklad, on_delete=models.CASCADE, related_name='sklads')

    def __str__(self):
        return self.image.url