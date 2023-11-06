from django.shortcuts import render

# Create your views here.
def index(request):
  
   return render(request, 'index.html')

def formulario (request):
   return render(request, 'formulario.html')