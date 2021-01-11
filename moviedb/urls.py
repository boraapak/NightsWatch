from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/comment',
         views.movie_comment, name='movie_comment'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]
