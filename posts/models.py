from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    is_admin = models.BooleanField(default=False)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    #Para realizar cambio en la base de datos AKA modelo
    # python3 manage.py makemigrations. Esto es para decir como, hey hice unos cambios
    #python3 manage.py migrate. Esto es para aplicar esos cambios a la base de datos
    #Ya luego se puede correr el servidor común y corriente
