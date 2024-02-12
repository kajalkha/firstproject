import json

from django.shortcuts import render, redirect
from . models import Form
from django.contrib import messages
from django.http import JsonResponse

from . import validation

# Create your views here.

#def app(request):
    #return HttpResponse('my name is sana')

def app_new(request):
    data = {'name':'kajal','address':'lalitpur'}
    return render(request,'first_application/index.html', {'data':data}) #if there is no keyword then it will show error
    
def index(request):
    if request.user.is_authenticated:
        return render(request,'first_application/index.html')
    else:
        return redirect("/login")
    
def home(request):
    if request.user.is_authenticated:
        return render(request,'first_application/home.html')
    else:
        return redirect("/login")

def about(request):
    if request.user.is_authenticated:
        return render(request,'first_application/about.html')
    else:
        return redirect("/login")

def contact(request):
    if request.user.is_authenticated:
        return render(request, 'first_application/contact.html')
    else:
        return redirect("/login")

def form(request):
    if request.user.is_authenticated:
        try:
            if request.method == "POST":        #shows error none in method using get 
                error_list, name, address, contact, email = validation.form_edit_create(request, None)
                if error_list:
                        return JsonResponse({"error":error_list}, status=400) 
                
                Form.objects.create(name = name, address= address, contact = contact, email = email)
                return JsonResponse({"response":"ok"},status=200)
        except Exception as exe:
            print(exe)
        return render (request, 'first_application/form.html')
    else:
        return redirect("/login")

def list1(request):
    if request.user.is_authenticated:
        data = Form.objects.filter(is_delete=False)           
        return render (request, 'first_application/list1.html',{'datas':data})
    else:
        return redirect("/login")

def edit_item(request, pk):
    if request.user.is_authenticated:
        tableform = Form.objects.get(id = pk, is_delete=False)
        if request.method == "POST":
            try:
                error_list, name, address, contact, email = validation.form_edit_create(request, pk)
                if error_list:
                        return JsonResponse({"error":error_list}, status=400)
                
                Form.objects.filter(id = pk, is_delete=False).update(name = name, address= address, contact =contact,   email = email)
                return JsonResponse({"response":"ok"},status=200)
            except Exception as exe:
                print(exe)
        return render (request, 'first_application/edit.html', {'tableform':tableform})   

def delete_item(request, pk):
    data = Form.objects.get(id=pk)
    data.is_delete=True
    data.save()
    messages.success(request, 'Data delete Successfully.')
    return redirect("/list1")





