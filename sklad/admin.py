from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 5





@admin.register(Sklad)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]

# Register your models here.
admin.site.register(CountrySklad)