from django.shortcuts import render, redirect
# To create a signup page - in django we have it inbuilt using below import 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.forms.fields import EmailField
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(request):
    if request.method == "POST":
        # form  = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome aboard, {username}")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form}) 

def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out Successfully")
    return redirect('food:index')