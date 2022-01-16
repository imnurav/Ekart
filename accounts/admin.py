from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account, MyAccountmanager

# Register your models here.


class AccountAdmin(UserAdmin):
    search_field = ('email', 'username',)
    list_display = ('email', 'username', 'last_login',
                    'date_joined', 'is_active',)
    list_display_links = ('email',)
    readmonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
