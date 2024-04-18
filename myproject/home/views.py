from django.shortcuts import render,redirect
from .models import Blog
from django.shortcuts import HttpResponse
from rest_framework import generics
from .models import student  
from .serializer import studentSerializer



# Create your views here.
def index(request):
    data={
        'blog':Blog.objects.all()
    }
    print(data)
    return render(request,"index.html",data)

def about(request):
    return render(request,"about.html")

def recent(request):
    return render(request,"recent_posts.html")

def add(request):
    return render(request,"add_posts.html")

def insert(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        image = request.FILES.get('image')  

        
        blog = Blog(title=title, description=description, date=date, image=image)
        blog.save()   
        return redirect('/')  

    

def find(request,id):
    fd={
        "data":Blog.objects.get(id=id)
    }
    return render(request,"find.html",fd)

def delete(request,id):
    dlt=Blog.objects.get(id=id)
    dlt.delete()
    return redirect("/")

def edit(request,id):
    ed={
        "data":Blog.objects.get(id=id)

    }            
    return render(request,"edit.html",ed)

def update(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        image = request.FILES.get('image')
        
        edit = Blog.objects.get(id=id)
        edit.title = title
        edit.description = description
        edit.date = date
        edit.image = image 
        edit.save()
        return redirect("/")  
class studentListAPI(generics.ListAPIView):
    queryset = student.objects.all()  
    serializer_class = studentSerializer    
    
class UserListAPI(generics.ListCreateAPIView):
    queryset = student.objects.all()  
    serializer_class = studentSerializer

class RetrieveStudentListAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()  
    serializer_class = studentSerializer
