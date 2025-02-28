from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.
def registerPage(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=first_name).exists():
            messages.error(request, "Username already taken!")
            return redirect("signup")

        user = User.objects.create_user(username=first_name, first_name = first_name, last_name = last_name, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect("login")
    return render(request, 'register.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html', {'error': 'Invalid email or password.'})   
    else: 
        return render(request, 'login.html')

def homePage(request):
    
    return render(request, 'home.html')

def forgotpasswordPage(request):
    return render(request, 'forgot-password.html')

def errorPage(request):
    return render(request, '404.html')

def addNote(request):
    return render(request, 'tasks/add_note.html')

def Add(request):
    return render(request, 'tasks/add.html')

def Delete(request):
    return render(request, 'tasks/delete.html')

def Detail(request):
    return render(request, 'tasks/detail.html')

def editNote(request):
    return render(request, 'tasks/edit_note.html')

def Edit(request):
    return render(request, 'tasks/edit.html')

def List(request):
    return render(request, 'tasks/list.html')

