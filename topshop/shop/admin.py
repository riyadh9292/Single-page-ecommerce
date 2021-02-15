from django.contrib import admin
from .models import Products,Order
# Register your models here.

admin.site.site_header = "Ecommerce site"
admin.site.site_title = "TopShop"
admin.site.index_title = "Manage TopShop"
class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    def change_description(self,request,queryset):
        queryset.update(description="This is the best product in business.")

    change_category_to_default.short_description = 'Default Category'
    change_description.short_description = 'default description'
    list_display = ('title','price','category','description','image')
    search_fields = ('title','category','price')
    actions = ('change_category_to_default','change_description')
    fields = ('title','price','category')
    list_editable = ('price','description','category','image')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('items','name','email','address','city','state','zipcode','total')
    list_editable = ('address','total')

admin.site.register(Products,ProductAdmin)
admin.site.register(Order,OrderAdmin)
