from django.shortcuts import render, redirect
from core.models import Claim,Request,modelQuestions,plan
from django.views.generic.edit import CreateView
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from django.contrib.auth import views as authh
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'core/main.html')

@login_required
def admnistrador(request):
    return render(request, 'gestion/index.html')

@login_required
def client(request):
    return render(request, 'gestion/lista_clientes.html')

@login_required
def on_hold(request):
    data = Claim.objects.all()
    return render(request, 'gestion/lista_reclamos.html', {'claims' : data})

@login_required
def reclamos_excedido(request):
    data = Claim.objects.filter( created__gte=datetime.now()-timedelta(days=1))
    return render(request, 'gestion/lista_reclamos.html', {'claims' : data})

@login_required
def reclamos_respondido(request):
    data = Claim.objects.filter( state=True)
    return render(request, 'gestion/lista_reclamos.html', {'claims' : data})

@login_required
def reclamos_questions(request):
    data = modelQuestions.objects.all()
    return render(request, 'gestion/tipo_pregunta.html', {'reclamos_questions' : data})


@login_required
def planess(request):
    data = plan.objects.all()
    return render(request, 'gestion/plan.html', {'planes' : data})

@login_required
def reclamo(request, pk):
    data = Claim.objects.get(pk=ObjectId(pk))
    if request.method == "POST":
        rpta = request.POST.get('respuesta')
        data.answers= {
        'answer': 'rpta',
        'files' : '',
        'created': '2020-08-07T22:51:25.522+00:00'
        }
        data.state = True
        data.save()
        return redirect('home')

    return render(request, 'gestion/rpta_reclamo.html', {'claims' : data})




def reclamos(request):
    
    data = modelQuestions.objects.all()
    if request.method == "POST":
            claim = Claim()
            claim.dni = request.POST.get('dni')
            claim.email = request.POST.get('email')
            claim.name = request.POST.get('nombre')
            preguntas = request.POST.getlist('caja')
            print(preguntas)
            claim.questions=[]
            data1= 0
            for p in preguntas:
                dic = {}
                info = modelQuestions.objects.get(pk=ObjectId(p))
                print(info.question)
                print(info.weighted)
                data1= data1 + info.weighted
                dic['question'] = info.question
                dic['weighted'] = info.weighted
                print(data1)
                claim.questions.append(dic)
            
            claim.priority = data1
            claim.save()
            return redirect('home')

    return render(request, 'core/reclamo.html', {'data' : data})

def solicitudes(request):

    data = plan.objects.all()
    if request.method == "POST":
            req = Request()
            req.dni = request.POST.get('dni')
            req.email = request.POST.get('email')
            req.name = request.POST.get('nombre')
            req.plan = request.POST.get('radio')     
            req.coin = request.POST.get('moneda')  
            req.save()
            return redirect('home')

    
    return render(request, 'core/solicitud.html', {'data' : data})


class login(authh.LoginView):
    redirect_authenticated_user = True
    template_name = 'core/login.html'

class logout(authh.LogoutView):
    template_name = 'core/logout.html'