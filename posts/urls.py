from django.urls import path
from posts import views

urlpatterns = [
    
    
    

    
    path(
        route='', 
        view=views.PostsFeedView.as_view(), 
        name='feed'
    ),

    path('posts/new',views.CreatePostView.as_view(), name='create'),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )

]