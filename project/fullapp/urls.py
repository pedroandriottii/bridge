from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signin, search, signup, demands, home, add_ambassador, add_manager, logout, index, demand_create, my_demands, signup_user2, demands_by_region, signup_user3, triagem, aprovar_triagem, rejeitar_triagem

urlpatterns = [
  path('signup/', signup, name="sign-up"),
  path('signin/', signin, name="sign-in"),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

  path('search/', search, name='search'),

  path('home/', home, name="home"),
  path('manager/add/', add_manager, name="add-manager"),
  path('demands/', demands, name="demands"),
  path('ambassador/add/', add_ambassador, name="add-ambassador"),
  path('demand/create/', demand_create, name='demand-create'),
  path('mydemands/', my_demands, name='my-demands'),
  path('', index, name="index"),
  path('signup_user2/', signup_user2, name='signup_user2'),
  path('signup_user3/', signup_user3, name='signup_user3'),
  path('demands/by-region/', demands_by_region, name='demands_by_region'),
  path('triagem/', triagem, name='triagem'),
  path('aprovar_triagem/<int:demand_id>/', aprovar_triagem, name='aprovar_triagem'),
  path('rejeitar_triagem/<int:demand_id>/', rejeitar_triagem, name='rejeitar_triagem'),
]