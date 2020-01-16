from django.urls import path
from users import views


urlpatterns = [


    

    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),


    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('me/profile', views.UpdateProfile.as_view(), name='update'),

    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]