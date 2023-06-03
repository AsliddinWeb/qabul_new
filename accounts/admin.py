from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User, UserVerification

# Excel
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields

from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse

class MyModelResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'name', 'created_at')

    def export_queryset(self, queryset):
        filtered_queryset = queryset.filter(is_authentication=1)
        return filtered_queryset

# class MyModelAdmin(ImportExportModelAdmin):
#     resource_class = MyModelResource

class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = MyModelResource
    add_form = UserCreationForm

    list_display = ('phone_number', 'name', 'image', 'created_at', 'is_verification')
    list_filter = ('is_verification', )
    fieldsets = (
        (None, {'fields': ('phone_number', 'name', 'image', 'is_verification', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'name', 'image', 'is_verification', 'password1', 'password2'),
        }),
    )
    ordering = ('-id',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)

class UserVerificationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code')

admin.site.register(UserVerification, UserVerificationAdmin)