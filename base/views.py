from django.shortcuts import render

# Create your views here.
def registerPage(request):
    return render(request, 'register.html')

def loginPage(request):
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

