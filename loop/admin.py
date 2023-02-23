from django.contrib import admin
from django import forms
from .models import Category, Product, User
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'name', 'price', 'in_stock', 'get_description', 'new_models', 'get_photo', 'quality', 'category',)
    list_display_links = ('id', 'name', 'category',)
    search_fields = ('name',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return 'нет фото'

    get_photo.short_description = 'миниатюра'

    def get_description(self, obj):
        return obj.description[:10]
    get_description.short_description = "description"


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'new_user')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'new_user')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
