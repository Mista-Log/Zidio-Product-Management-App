from django.urls import path
from . import views



urlpatterns = [
    path('', views.loginPage),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('home/', views.homePage, name="home"),
    path('forgot-password/', views.forgotpasswordPage, name="forgot-password"),
    path('404/', views.errorPage, name="404"),

    path('add_note/', views.addNote, name="add_note"),
    path('add/', views.Add, name='add'),
    path('delete/', views.Delete, name='delete'),
    path('detail/', views.Detail, name='detail'),
    path('edit_note/', views.editNote, name="edit_note"),
    path('edit/', views.Edit, name='edit'),
    path('list/', views.List, name='list'),
]




