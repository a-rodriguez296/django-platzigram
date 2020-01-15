from django.urls import path
from posts import views

urlpatterns = [
    
    
    

    
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),

    path('posts/new',views.create_post, name='create'),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )

]