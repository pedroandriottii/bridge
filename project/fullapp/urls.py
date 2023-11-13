from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signin, signup, demands, home, add_embassador, add_manager, logout, index, demand_create, my_demands, signup_user2, demands_by_region, signup_user3

urlpatterns = [
  path('signup/', signup, name="sign-up"),
  path('signin/', signin, name="sign-in"),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

  path('home/', home, name="home"),
  path('manager/add/', add_manager, name="add-manager"),
  path('demands/', demands, name="demands"),
  path('embassador/add/', add_embassador, name="add-embassador"),
  path('demand/create/', demand_create, name='demand-create'),
  path('mydemands/', my_demands, name='my-demands'),
  path('', index, name="index"),
  path('signup_user2/', signup_user2, name='signup_user2'),
  path('signup_user3/', signup_user3, name='signup_user3'),
  path('demands/by-region/', demands_by_region, name='demands_by_region'),
]