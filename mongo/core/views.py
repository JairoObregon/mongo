from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/main.html')

def admnistrador(request):
    return render(request, 'admin/index.html')

def client(request):
    return render(request, 'admin/clients.html')
