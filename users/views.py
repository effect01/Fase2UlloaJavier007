from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import  authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            print('hola')
            login(request,user)
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Tu cuenta a sido creada, {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

            
    return render(request = request, template_name= 'users/register.html', context={'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')
