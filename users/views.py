from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, FormView, UpdateView


#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Forms
from users.forms import SignupForm

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



class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    model = Profile
    #No entiendo muy bien pq esto reemplaza el form
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        #REturn users profile
        return self.request.user.profile

    def get_success_url(self):
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})




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


class SignUpView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

