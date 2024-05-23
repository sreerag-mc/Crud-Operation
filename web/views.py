from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm


def addshow(request):
    if request.method=='POST':
        fm= UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm=UserForm()

    else:
        fm = UserForm()  # Corrected form instantiation
    return render(request, 'show.html', {'form': fm})

def display(request):
    stud=User.objects.all()
    return render(request,'display.html',{'stud':stud})


def delete_data(request,id):
    pi=User.objects.get(pk=id)
    pi.delete()
    return redirect('display')

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=UserForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('display')
    else:
        pi=User.objects.get(pk=id)
        fm=UserForm(instance=pi)
    return render(request,'updateindex.html',{'form':fm})