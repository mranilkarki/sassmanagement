from django.shortcuts import render
from records.models import list_students,image_students
from .forms import listForm,ImageForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required





def students_list(request):
    list= list_students.objects.all()
    images = image_students.objects.all()
    
    return render(request, 'records/sasslist.html', {'list': list,'images':images})

def login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
             return redirect('/editmode1/')
    else:
         form= AuthenticationForm()
    return render(request, 'records/login.html',{'form':form})  
    

def register(request):
    if request.method== "POST":
        form= listForm(request.POST)
        if form.is_valid():
             
            list_students= form.save(commit=True)
            list_students.save()
            return redirect('/list/',)
            
    else:
        form= listForm()
        return render(request, 'records/register.html', {'form': form},)


@login_required(login_url='records:login')
def editmode(request):
    list= list_students.objects.all()
    images = image_students.objects.all()
    return render(request, 'records/editmode.html', {'list': list,'images':images})


def editmode1(request):
    list= list_students.objects.all()
    images = image_students.objects.all()
    return render(request, 'records/editmode.html', {'list': list,'images':images})
      

def upload(request):
     if request.method == 'POST':
        imgform = ImageForm(request.POST, request.FILES)
        if imgform.is_valid():
           
            imgform.save()
            
            return redirect('/list/',)
     else:
        imgform = ImageForm() # A empty, unbound form
        return render(request, 'records/upload.html',{'imgform':imgform})



    
  


def delete(request, pk):
   
    object = get_object_or_404(list_students, pk=pk)
    if request.method== "POST":
        object.delete()
        
        messages.success(request, 'messages successfully deleted')
        return redirect('/list/')
        
    else:
        
        return render(request, 'records/delete.html')



def edit(request, pk):
   
    list = get_object_or_404(list_students, pk=pk)
    if request.method == "POST":
        form = listForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save(commit=True)
            list.name= str(request.user)
            
            return redirect('/list/')        
            
    else:
        form = listForm(instance=list)
    return render(request, 'records/register.html', {'form': form})

def search(request):
    if request.method=='POST':
        value= request.POST['name']
        if value:
            match= list_students.objects.filter(Q(name__icontains=value)  | Q(family_history__icontains=value))
            if match:
                return render(request,'records/search.html',{'srch':match})
            else:
                messages.error(request, "no match results")
        else:
            return redirect('/search/')    
    else:
        return render(request, 'records/sasslist.html')










    


