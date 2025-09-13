
from django.urls import path
from .views import game_list, signup_view, login_view, logout_view, game_detail

urlpatterns = [
    path('', game_list, name='landing'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('games/', game_list, name='game_list'),
    path('<int:pk>/', game_detail, name='game_detail'),
]
