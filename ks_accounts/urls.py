from django.urls import include, path

import ks_accounts.views

app_name='accounts'

urlpatterns = [
    path('login/', ks_accounts.views.ks_login, name="login"),
    path('signup/', ks_accounts.views.signup, name="signup"),
    path('logout/', ks_accounts.views.signup, name="logout"),
]