from django.contrib import admin

from users.models import Profile

# Register your models here.

#Esto se hace para customizar el admin. Las clases deben terminar en Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    #Columnas que se muestran en el administrador
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    #Links que me van a llevar al detalle de usuario
    list_display_links = ('pk', 'user')

    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__username',
        'user__email', 
        'user__first_name', 
        'user__last_name', 
        'phone_number')

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified')
