from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import userForm,EditForm

def signup(request):
    if request.method=="GET":
        form=userForm()
        return render(request,'signup.html',{"form":form})
    else:
        form=userForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            confirm_password=form.cleaned_data['password2']
            form.save()
            return render(request,'signup.html',{"form":form})
        return HttpResponse("Password should be of 8 characters")

def login_user(request):
    if not request.user.is_authenticated:
        if request.method=="GET":
            form=AuthenticationForm()
            return render(request,'login.html',{"form":form})
        form=AuthenticationForm(request.POST,data=request.POST)
        if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    request.session['username']=username
                    return redirect('/user_profile/')
                else:
                    return HttpResponse("Invalid")
        else:
            return HttpResponse("Invalid")
    else:
        return redirect('/user_profile/')
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=EditForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
        else:
            form=EditForm(instance=request.user)
        return render(request,'index.html',{'name':request.user,'form':form})
    return redirect('/login/')

def user_logout(request):
    logout(request)
    return redirect("/login/")




