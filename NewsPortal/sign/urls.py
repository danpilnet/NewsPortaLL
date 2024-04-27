from django.urls import path
from django.contrib.auth.views import TemplateView
from. views import BaseRegisterView, logout_view
from .views import upgrate_me

urlpatterns = [
    path('login/', BaseRegisterView.as_view(template_name='login.html'),
         name= 'login'),
    path('logout/', logout_view, name='logout'),

    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'),
         name= 'signup'),
    path('logout/confirm/', TemplateView.as_view(template_name='logout_confirm.html'),
         name='logout_confirm'),
    path('upgrate/', upgrate_me, name='upgrate'),
]