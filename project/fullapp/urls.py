from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signin, signup, hom, add_manager, logout, index, demand_create, my_demands

urlpatterns = [
  path('signup/', signup, name="sign-up"),
  path('home/', hom, name="home"),
  path('manager/add/', add_manager, name="add-manager"),
  path('signin/', signin, name="sign-in"),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('demand/create/', demand_create, name='demand-create'),
  path('my-demands/', my_demands, name='my-demands'),
  path('', index, name="index"),
]