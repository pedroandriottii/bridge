from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  # path('', views.home, name="home"),
  path('sign-up/', views.signup, name="signup"),
  path('manager/add/', views.add_manager, name="add-manager"),
  path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name="login"),
  # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]