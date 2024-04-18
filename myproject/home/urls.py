from django.contrib import admin
from django.urls import path
from . import views
from .views import studentListAPI,UserListAPI,RetrieveStudentListAPI




urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('recent/',views.recent,name="recent"),
    path('add/',views.add,name="add"),
    path('find/<id>',views.find,name="find"),
    path('insert',views.insert),
    path('delete/<id>', views.delete, name="delete"),
    path('edit/<id>',views.edit,name="edit"),
    path('update/<id>',views.update,name="update"),
    path('student/',studentListAPI.as_view()),
    path('ss',UserListAPI.as_view()),
    path('ss/<pk>',RetrieveStudentListAPI.as_view())
  
]
