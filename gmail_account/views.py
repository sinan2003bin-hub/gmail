from urllib import request

from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    if request.method == "POST":
        gmail = request.POST["gmail"]
        password = request.POST["password"]

        user = authenticate(
            request,
            gmail=gmail,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect("dashboard")
        
        return render(request, "home.html", 
                {
                    "error": "Password or username is incorrect"
                }
            )
    
    return render(request, "home.html")

def signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        gmail = request.POST["gmail"]

        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if len(password) < 8:
            return render(request,"signup.html",
                {
                    "error": "Password must be at least 8 characters"
                }
            )

        if not any(char.isupper() for char in password):
            return render(request,"signup.html",
                {
                    "error":"Password must contain at least 1 uppercase letter"
                }
            )

        if not any(char.isdigit() for char in password):
            return render(request,"signup.html",
                {
                    "error":"Password must contain at least 1 number"
                }
            )

        special_chars = "!@#$%^&*"

        if not any(char in special_chars for char in password):
            return render(request,"signup.html",
                {
                    "error": "Password must contain at least 1 special character"
                }
            )
        
        if password != confirm_password:

            return render(request,"signup.html",
                {
                    "error":"Passwords do not match"
                }
            )

        User.objects.create_user(
            username=username,
            gmail=gmail,
            password=password,
        )

        return redirect("home")
    return render(request, "signup.html")

@login_required
def dashboard(request):
    return render(request,"dashboard.html")

def logout_page(request):

    logout(request)

    return redirect("home")
