from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from ks_accounts.forms import CustomUserCreationForm
from ks_accounts.models import User


def main_page(request):
    return render(request, 'ks_accounts/main.html', {})

def ks_login(request):
    if request.method=="GET":
        loginForm = AuthenticationForm()
        return render(request, 'ks_accounts/login.html')

    elif request.method=="POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            login(request, loginForm.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("/home/")
        return render(request, 'ks_accounts/login.html')

def ks_logout(request):
    logout(request)
    if 'next' in request.POST:
        return redirect(request.POST.get('next'))
    return redirect("/home/")


def signup(request):
    if request.method=="GET":
        signup_form = CustomUserCreationForm()
        context = {'signupForm':signup_form}
        return render(request, 'account/signup.html', context)

    elif request.method=="POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            return redirect('/home/')
        else:
            return HttpResponse(signup_form)