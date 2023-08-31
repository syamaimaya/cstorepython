from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Department, Courses, Product
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import Register


# Create your views here.
def dept(request):
    data = Department.objects.all()
    return render(request, 'department.html', {'data': data})


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Registration Succesfull.")
            return redirect('Cstoreapp:login')
    else:
        form = Register()
    return render(request, "register.html", {'form': form})

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request, user)
            messages.success(request, f'welcome {username}')
            return redirect('Cstoreapp:shop')
        else:
            return redirect('Cstoreapp:shop')
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})



def shop(request):
    return render(request, "shop.html")


def order(request):
    template_name='order.html'
    data = Department.objects.all()
    sub=Courses.objects.all()
    Product.objects.all()
    return render(request,"order.html", {"data": data,"sub":sub})

def status(request):
    return render(request,"status.html")