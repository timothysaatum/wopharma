from django.contrib import admin
from .models import Pharmacy, DrugCategory, Drug, Prescriptions, Tag



class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pharmacy_name', 'digital_address', 'registration_code', 'region')


class DrugCategoryAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'drug_class', 'general_description')


class DrugAdmin(admin.ModelAdmin):
    list_display = ('category', 'drug_name', 'price', 'discount_percentage', 'expiry_date', 'quantity_in_stock', 'side_effect', 
        'apply_discount', 'is_in_stock', 'publish')


class PrescriptionsAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'drug', 'created_on', 'prescribed_by', 'precribed_to', 'precribed_for', 'dosage', 'relevant_advice')


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(DrugCategory, DrugCategoryAdmin)
admin.site.register(Drug, DrugAdmin)
admin.site.register(Prescriptions, PrescriptionsAdmin)
admin.site.register(Tag, TagAdmin)
