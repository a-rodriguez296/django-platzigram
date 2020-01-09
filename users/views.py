from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Forms
from users.forms import ProfileForm, SignupForm

#Exception
from django.db.utils import IntegrityError

# Create your views here.

@login_required
def update_profile(request):
    
    profile = request.user.profile

    #Si me llega un post, analizo los datos y hago algo con ellos
    if request.method == 'POST':
        
        #El request.files es para el archivo de la imagen
        form = ProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.cleaned_data
            
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            #Para evitar que el formulario sea renviado hay que hacer un refirect
            return redirect('update_profile')




    #De lo contrario pinto el form vacio
    else:
        form = ProfileForm()


    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            #Se agrega el form en el contexto para q esté disponible en el template
            'form':form
        }
    )


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        user = authenticate(request, username=username, password=password)
        if user:
            # Esta linea crea la sesión
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form':form
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

