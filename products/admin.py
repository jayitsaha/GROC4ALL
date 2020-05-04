from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id' , 'title' , 'slug')
	prepopulated_fields = {"slug": ("title",)}
	list_display_links = ('id' , 'title')
	list_filter = ('title',)
	list_editable = ('slug',)
	search_fields = ('title','slug')
	list_per_page = 25


# Register your models here.
admin.site.register(Product , ProductAdmin)
