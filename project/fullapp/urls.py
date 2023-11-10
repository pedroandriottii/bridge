from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signin, signup, hom, add_manager, logout, create_request, index

from . import views

urlpatterns = [
  path('signup/', signup, name="sign-up"),
  path('', index, name="index"),
  path('home/', hom, name="home"),
  path('manager/add/', add_manager, name="add-manager"),
  path('login/', signin, name="login"),
  path('solicitacao/<int:project_id>/', create_request, name='solicitacao'),
  path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]