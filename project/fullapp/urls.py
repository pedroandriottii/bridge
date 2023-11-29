from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signin, search, project_details, signup, demands, home, add_ambassador, add_manager, logout, demand_create, demands_by_region, triagem, aprovar_triagem, rejeitar_triagem, demand_detail

urlpatterns = [
  path('signup/', signup, name="sign-up"),
  path('', signin, name="sign-in"),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('search/', search, name='search'),
  path('home/', home, name="home"),
  path('manager/add/', add_manager, name="add-manager"),
  path('demands/', demands, name="demands"),
  path('ambassador/add/', add_ambassador, name="add-ambassador"),
  path('demand/create/', demand_create, name='demand-create'),
  path('demands/by-region/', demands_by_region, name='demands_by_region'),
  path('triagem/', triagem, name='triagem'),
  path('aprovar_triagem/<int:demand_id>/', aprovar_triagem, name='aprovar_triagem'),
  path('rejeitar_triagem/<int:demand_id>/', rejeitar_triagem, name='rejeitar_triagem'),
  path('demand/<int:demand_id>/', demand_detail, name='demand_detail'),
  path('project/<int:id>/', project_details, name='project_detail'),
]