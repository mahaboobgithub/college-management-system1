from django.shortcuts import render,redirect
from hod.forms import HODForm
from hod.SampleMiddleware import my_location

def showLogin(request):
    cname = my_location()
    return render(request,"hod/login.html",{"cname":cname})


def hod_register(request):
    return render(request,"hod/hod_register.html",{"form":HODForm()})


def save_hod(request):
    hod = HODForm(request.POST)
    if hod.is_valid():
        hod.save()
        return redirect("main")
    else:
        return render(request, "hod/hod_register.html", {"form": hod})
