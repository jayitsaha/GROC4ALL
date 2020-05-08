from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
	list_display = ('id' ,'item' ,'quantity','price','total','name','phone','email','address')
	list_display_links = ('id' , 'item')
	list_filter = ('item',)
	#list_editable = ('item',)
	search_fields = ('item','name')
	list_per_page = 25


# Register your models here.
admin.site.register(Order , OrderAdmin)
