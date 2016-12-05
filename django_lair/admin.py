from django.contrib import admin
from .models import User, Datum


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid')
    search_fields = ('uuid',)
admin.site.register(User, UserAdmin)


class DatumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'user', 'created')
    search_fields = ('name', 'value', 'user')
admin.site.register(Datum, DatumAdmin)
