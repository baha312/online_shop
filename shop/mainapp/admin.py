from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django import forms
from django.forms import ModelChoiceField, ModelForm
# Register your models here.
from .models import *

class ChipsCategoryChoiceField(forms.ModelChoiceField):
    pass


class ChipsAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='chips'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class JamCategoryChoiceField(forms.ModelChoiceField):
    pass

class JamAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='jam'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Chips, ChipsAdmin)
admin.site.register(Jam, JamAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)