from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

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

    fieldsets = (
        ('Profile', {
            'fields' : ('user', 'picture')
        }),
        ('Extra info' , {
            'fields' : (
                ('website', 'phone_number'),
                ('biography')
            )
        }), 
        ('Metadata', {
            'fields' : (
                #Como estas dos variables no se pueden editar, hay que crear un readonly
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created', 'modified', 'user')

    #Esto es para que se pueda crear el profile y el user en la misma pantalla.
    #Si no hago esto, me toca crear el user por un lado y después crear el profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'



class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


#Lo que hay que hacer es hacer unregister del User
admin.site.unregister(User)

#Luego registrarlo pero como userAdmin
admin.site.register(User, UserAdmin)

    
