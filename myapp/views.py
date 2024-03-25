from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from user.models import User,Producto,userEmpleado
from django.db import IntegrityError
#my personal form
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html');
def signup(request):
    if request.method=="GET":
        return render(request,'signup.html',{
            'form':CustomUserCreationForm
        });
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'],
                                              first_name=request.POST['first_name'],
                                              last_name=request.POST['last_name'],
                                              email=request.POST['email'],
                                              password=request.POST['password1'],
                                              usertype=request.POST['usertype']
                                              )
                if 'picture' in request.FILES:
                    user.picture=request.FILES['picture']
                if request.POST['usertype']=='empleado':
                    cliente=userEmpleado(user=user)
                    cliente.save()
                login(request,user)
                user.save()
                return redirect('home');
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form':CustomUserCreationForm,
                    'error':'User already exists'
                })
        return render(request, 'signup.html',{
            'form':CustomUserCreationForm,
            'error':'password do not match'
        })
def signin(request):
    if request.method=='GET':
        return render(request, 'signin.html',{
            'form':AuthenticationForm,
            'error':"Username or password is incorrect"
        })
    else:
        user=authenticate(request,username=request.POST['username'], password=request.POST['password']);
        if user is None:
            return render(request,'signin.html',{
                'form':AuthenticationForm,
                'error':"Username or password is incorrect"
            })
        else:
            login(request,user)
            return redirect('home')
def buscador(request):
    productos=[];
    cant_productos=0;
    cant_mensaje="";
    if request.method=='GET':
        query_nombre=request.GET.get('nombre','').strip();
        query_precio=request.GET.get('precio','').strip();
        query_cantidad=request.GET.get('cantidad','').strip()
        
        #parámetro de busqueda
        if query_nombre or query_precio or query_cantidad:
            productos=Producto.objects.all();
            if query_nombre:
                productos = productos.filter(nombre__icontains=query_nombre),
                productos = productos.filter(precio__icontains=query_precio),
                productos = productos.filter(cantidad__icontains=query_cantidad)
        cant_productos=len(productos);
        if cant_productos>1:
            cant_mensaje="resultados";
        elif cant_productos==1:
            cant_mensaje="resultado";
    return render(request, 'search.html',{
        'productos':productos,
        'cant_productos':cant_productos,
        'cant_mensaje':cant_mensaje
    })

