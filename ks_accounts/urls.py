from django.urls import include, path

import ks_accounts.views

app_name='accounts'

urlpatterns = [
    path('logout/', ks_accounts.views.ks_logout, name="logout"),
]