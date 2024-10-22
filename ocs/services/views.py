from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"services/index.html")
def appointments(request):
    pass
def login(request):
    pass
def signup(request):
    pass