from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from poll_app.models import Question,Options
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@login_required(redirect_field_name='login/')
def index(request):
    q=Question.objects.all()
    d={}
    d['questions']=q;
    return render(request,'index.html',context=d)

def inc_vote(request,pk):
    q=Options.objects.get(pk=pk)
    q.votes=q.votes+1
    q.save()
    return HttpResponseRedirect(reverse('index'))

def add_ques(request):
    q=request.GET.get('question')
    obj=Question(question=q)
    obj.save()
    return HttpResponseRedirect(reverse('index'))

def add_option(request,pk):
    q=Question.objects.get(pk=pk)
    option=request.GET.get('option')
    obj=Options(option=option)
    obj.question=q
    obj.save()
    return HttpResponseRedirect(reverse('index'))


def result(request,pk):
    q=Question.objects.get(pk=pk)
    d={}
    d['q']=q;
    return render(request,'result.html',context=d)

def register(request):
    if request.method=='POST':
        obj=User()
        print(request.POST)
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        obj.username=uname
        obj.password=upass
        obj.set_password(obj.password)
        obj.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request,'register.html')


def user_login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        user=authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse("<h1>Wrong Password or Username</h1>")
    else:
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
