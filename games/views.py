
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Game


def landing(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, "landing.html", {"login_form": login_form, "signup_form": signup_form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('game_list')
    else:
        form = UserCreationForm()
    return render(request, 'singup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('game_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landing')
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_detail.html', {'game': game})
@login_required(login_url='login')
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

