from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout

from ks_accounts.forms import CustomUserCreationForm


def main_page(request):
    return render(request, 'ks_accounts/main.html', {})

def ks_login(request):
    if request.method=="GET":
        loginForm = AuthenticationForm()
        context = {'loginForm':loginForm}
        return render(request, 'ks_accounts/login.html', context)

    elif request.method=="POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            login(request, loginForm.get_user())

def ks_logout(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method=="GET":
        signup_form = CustomUserCreationForm()
        context = {'signupForm':signup_form}
        return render(request, 'ks_accounts/sign_up.html', context)

    elif request.method=="POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            return HttpResponse("저장완료")
        else:
            return HttpResponse(signup_form)