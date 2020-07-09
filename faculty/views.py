from django.shortcuts import render
from faculty.form import FacultyForm


def faculty_login(request):
    return render(request,"faculty/login.html")


def faculty_register(request):
    return render(request,"faculty/faculty_register.html",{"form":FacultyForm()})