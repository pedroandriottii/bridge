from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('sign-up/', views.signup, name="signup"),
  path('', views.hom, name="home"),
  path('manager/add/', views.add_manager, name="add-manager"),
  path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
  path('solicitacao/',views.solicitacao, name = "solicitacao"),
  
]