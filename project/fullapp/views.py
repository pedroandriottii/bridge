from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import SignupForm

# Create your views here.
def signup(request):
  if request.method == 'POST':
    print(request.POST)

    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      print("criou")

      return redirect("signup")

  return render(request, 'auth/signup.html')

@login_required
def add_manager(request):
  current_user = request.user

  print(current_user.role)

  if current_user.role != 1:
    return redirect("login")

  return render(request, 'management/add-manager.html')