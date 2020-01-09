from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignupForm

#Exception
from django.db.utils import IntegrityError

# Create your views here.






class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'


    def get_context_data(self, **kwargs):

        #Esto se hacee con el objetivo de agregar al contexto los posts de ese usuario y poderlos pintar
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context




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

            #Para evitar que el formulario sea renviado hay que hacer un redirect

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)




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
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
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
    return redirect('users:login')

