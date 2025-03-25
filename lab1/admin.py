from django.contrib import admin
from .models import Market, Product, ContactInfo, MarketProduct, Employee

# Register your models here.


class MarketProductInline(admin.TabularInline):
    model = MarketProduct
    extra = 1  # Додава празно поле за нов внес

class MarketAdmin(admin.ModelAdmin):
        list_display = ("name", )
        inlines = [MarketProductInline]

        def has_delete_permission(self, request, obj=None):
            if request.user.is_superuser:
                return True
            return False

        def has_add_permission(self, request):
            if request.user.is_superuser:
                return True
            return False

        def save_model(self, request, obj, form, change):
            if not change:  # Само при креирање на нов маркет
                obj.user = request.user
            obj.save()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")


    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if not change:  # Само при креирање на нов вработен
            obj.user = request.user
        obj.save()

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "product_type", "homeMade")
    list_filter = ("product_type", "homeMade")

class ContactInfoAdmin(admin.ModelAdmin):
        list_display = ("street", "phone", "email")


admin.site.register(Market, MarketAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(MarketProduct)