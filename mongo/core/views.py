from django.shortcuts import render, redirect
from core.models import Claim,Request,modelQuestions,plan
from django.views.generic.edit import CreateView
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from django.contrib.auth import views as authh
from django.contrib.auth.decorators import login_required
import datetime
#email
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    return render(request, 'core/main.html')

@login_required
def admnistrador(request):
    return render(request, 'gestion/index.html')


#client list
@login_required
def client(request):
    return render(request, 'gestion/lista_clientes.html')

#claim list unanswered
@login_required
def on_hold(request):
    data = Claim.objects.filter(rpta=False, state=1)
    if request.method == "POST":
        pk = request.POST.get('object')
        dat = Claim.objects.get(pk=ObjectId(pk))
        dat.state = 2
        dat.save()
        return redirect('gestion')
    return render(request, 'gestion/lista_reclamos.html', {'claims' : data})

#claim list derived to the legal area
@login_required
def legal(request):
    data = Claim.objects.filter(rpta=False, state=2)
    return render(request, 'gestion/legal.html', {'claims' : data})

#claim list days exceeded 
@login_required
def reclamos_excedido(request):
    data = Claim.objects.filter( created__gte=datetime.now()-timedelta(days=1))
    return render(request, 'gestion/lista_reclamos_excedido.html', {'claims' : data})

#claim list answered
@login_required
def reclamos_respondido(request):
    data = Claim.objects.filter( rpta=True)
    return render(request, 'gestion/lista_relclamos_contestado.html', {'claims' : data})

#questions list
@login_required
def reclamos_questions(request):
    data = modelQuestions.objects.all()
    return render(request, 'gestion/tipo_pregunta.html', {'reclamos_questions' : data})

#plan list
@login_required
def planess(request):
    data = plan.objects.all()
    return render(request, 'gestion/plan.html', {'planes' : data})

#specific claim
@login_required
def reclamo(request, pk):
    data = Claim.objects.get(pk=ObjectId(pk))
    if request.method == "POST":
        rpta = request.POST.get('respuesta')
        files = request.FILES['files']
        data.answers= {
        'answer': rpta,
        'files' : files,
        'created': datetime.datetime.now()
        }
        data.state=3
        data.rpta = True
        data.save()

        email = EmailMessage(
              
                subject='mongodb',
                body=rpta  ,
                from_email=data.email,
                to=['kayn.g4@gmail.com']
            )
        email.attach('invoicex.pdf', files.read() , 'application/pdf')
        email.content_subtype = 'html'
        email.send()
        return redirect('home')


    return render(request, 'gestion/rpta_reclamo.html', {'claims' : data})



#form Claim
def reclamos(request):
    
    data = modelQuestions.objects.all()
    if request.method == "POST":
            claim = Claim()
            claim.dni = request.POST.get('dni')
            claim.email = request.POST.get('email')
            claim.name = request.POST.get('nombre')
            preguntas = request.POST.getlist('caja')
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
            claim.files=request.FILES['filesS']
            claim.state=1
            claim.save()
            return redirect('home')

    return render(request, 'core/reclamo.html', {'data' : data})


#form Request
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



#client Request unanswered
@login_required
def on_hold_plan(request):
    data = Request.objects.filter( rpta=False)
    return render(request, 'gestion/lista_atencion.html', {'data' : data})



#client Request days exceeded 
@login_required
def atencion_excedido(request):
    data = Request.objects.filter( created__gte=datetime.now()-timedelta(days=1))
    return render(request, 'gestion/lista_atencion_excedido.html', {'data' : data})

#claim list answered
@login_required
def atencion_respondido(request):
    data = Request.objects.filter( rpta=True)
    return render(request, 'gestion/lista_atencion_contestado.html', {'data' : data})



#login
class login(authh.LoginView):
    redirect_authenticated_user = True
    template_name = 'core/login.html'

#logout
class logout(authh.LogoutView):
    template_name = 'core/logout.html'

#State claim or request
def state(request,dni):
    data = Claim.objects.filter(dni=dni)
    data1 = Request.objects.filter(dni=dni)
    return render(request, 'core/state.html', {'data' : data,'data1' : data1 })


#form State 
def template_state(request):
    if request.method == "POST":
            data = request.POST.get('dni')
            if(Claim.objects.filter(dni=data) or Request.objects.filter(dni=data)):
                return redirect('state', dni=data)
            else:
                return redirect('/template_state/?error')
    return render(request, 'core/template_state.html')
    