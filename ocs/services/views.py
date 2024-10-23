from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def index(request):
    # Check if the user is signed in by looking for 'username' in the session
    if 'username' not in request.session:
        # If not signed in, redirect to the login page
        return redirect(reverse("login"))
    
    usrName = request.session.get('username')  # Retrieve username from session
    return render(request, "services/index.html", {"usrName": usrName})

def appointments(request):
    # Check if the user is signed in
    if 'username' not in request.session:
        return redirect(reverse("login"))
    
    return render(request, "services/appointments.html")

def login(request):
    # If the user is already signed in, redirect them to the index page
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pswd"]
        
        try:
            # Fetch the user from the database by email
            usr = User.objects.get(email=email)
            
            # Check if the provided password matches the stored hashed password
            if check_password(password, usr.pswd):
                # Store the username in the session
                request.session['username'] = usr.usrName
                
                # Redirect to the index page
                return redirect(reverse("index"))
            else:
                # Invalid password case
                return render(request, "services/login.html", {"error": "Invalid password"})
        except User.DoesNotExist:
            # User not found case
            return render(request, "services/login.html", {"error": "User does not exist"})
    
    return render(request, "services/login.html")

def signup(request):
    # If the user is already signed in, redirect them to the index page
    if 'username' in request.session:
        return redirect(reverse("index"))
    
    if request.method == "POST":
        usrName = request.POST.get("username")
        email = request.POST.get("email")
        pswd = request.POST.get("pswd")
        cnpswd = request.POST.get("cnpswd")
        
        # Check if passwords match
        if pswd != cnpswd:
            return render(request, "services/signup.html", {"error": "Passwords do not match"})
        
        # Check if username or email already exists in your custom User model
        if User.objects.filter(usrName=usrName).exists():
            return render(request, "services/signup.html", {"error": "Username already taken"})
        if User.objects.filter(email=email).exists():
            return render(request, "services/signup.html", {"error": "Email already registered"})
        
        # Hash the password before saving
        hashed_pswd = make_password(pswd)
        
        # Create a new user in your custom User model
        user = User(usrName=usrName, email=email, pswd=hashed_pswd)
        
        # Save the user to the database
        user.save()

        # Store the username in the session
        request.session['username'] = usrName

        # Redirect to the login page
        return redirect(reverse("login"))
    
    return render(request, "services/signup.html")

def logout(request):
    # Remove the username from the session to log the user out
    request.session.flush()  # This will clear all session data
    return redirect(reverse("login"))
