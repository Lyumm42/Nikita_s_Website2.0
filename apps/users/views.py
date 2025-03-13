from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUCF, CustomUChangeF




def register(request):
    if request.method == 'POST':
        form = CustomUCF(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUCF()
    return render(request, 'users/register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    return render(request, 'users/login.html')





def user_logout(request):
    logout(request)
    return redirect('home')