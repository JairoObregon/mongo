from django.shortcuts import render, redirect
from core.models import Claim
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return render(request, 'core/main.html')

def admnistrador(request):
    return render(request, 'lte/index.html')

def client(request):
    return render(request, 'lte/clients.html')


class ClaimCreate(CreateView):
    model = Claim
    fields = ['dni','email','name','message','files']



def reclamos(request):
    
    if request.method == "POST":
            claim = Claim()
            claim.dni = request.POST.get('dni')
            claim.email = request.POST.get('email')
            claim.name = request.POST.get('nombre')
            preguntas = request.POST.getlist('caja')
            print(claim.dni)
            print(claim.email)
            print(preguntas)
            claim.questions=[]
            for i in preguntas:
                print(i)
                dic = {}
                if i == '1':
                    dic['question'] = "Option 1"
                    dic['weighted'] = 1
                
                if i == '2':
                    dic['question'] = "Option 2"
                    dic['weighted'] = 2

                if i == '3':
                    dic['question'] = "Option 3"
                    dic['weighted'] = 3
                
                print(dic)
                claim.questions.append(dic)
            
            claim.save()
            return redirect('http://127.0.0.1:8000/')

    return render(request, 'core/reclamo.html')

def solicitudes(request):
    return render(request, 'core/solicitud.html')
