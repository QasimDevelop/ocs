from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"services/index.html")
def appointments(request):
    return render(request,"services/appointments.html")
def login(request):
    return render(request,"services/login.html")
def signup(request):
    return render(request,"services/signup.html")