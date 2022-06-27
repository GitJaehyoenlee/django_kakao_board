from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import login

# Create your views here.
def main_page(request):
    return render(request, 'ks_accounts/main.html', {})

# def ks_login(request):
#     if request.method=="GET":
#         loginForm = AuthenticationForm()
#         context = {'loginForm':loginForm}
#         return render(request, 'user/login.html', context)
#
#     elif request.method=="POST":
#         loginForm = AuthenticationForm(request, request.POST)
#         if loginForm.is_valid():
#             login(request, loginForm.get_user())

