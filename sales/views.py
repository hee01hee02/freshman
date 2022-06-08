import imp
from multiprocessing import context
from typing_extensions import Self
from django.shortcuts import render,redirect,reverse
from django.http import HttpRequest
from django.http.response import HttpResponse

from freshman.auth.forms import UserCreationForm
from .models import Sale, Person
from .forms import SaleForm,SaleModelForm
from django.views import generic






class IndexView(generic.TemplateView):
    template_name = "index.html"

def Index(request):
  return render(request,"index.html")  

class SaleListView(generic.ListView):
    template_name = "folder/salelist.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"

def SaleList(request):
    회원 = Sale.objects.all()
    context = {
        "사람키" : 회원
        
        
    }
    return render(request,"folder/salelist.html",context)

class SaleNoticeView(generic.DetailView):
    template_name = "folder/salenotice.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"

def SaleNotice(request, pk):
      
    회원 = Sale.objects.get(id=pk)  
    context = {
        "사람키" : 회원
        
    } 
    return render(request,"folder/salenotice.html",context)

class SaleInputView(generic.CreateView):
    template_name = "folder/saleinput.html"
    form_class = SaleModelForm
    def get_success_url(self) :
        return reverse("homepage:List")

def SaleInput(request):
    폼 = SaleModelForm()
    if request.method == "POST":
        
        폼 = SaleModelForm(request.POST)
        if 폼.is_valid():

            폼.save()

            return redirect("/homepage")
    context = {
        "폼키" : 폼

    }
    return render(request,"folder/saleinput.html",context) 

class SaleUpdateView(generic.UpdateView):
    template_name = "folder/saleupdate.html"
    queryset = Sale.objects.all()
    form_class = SaleModelForm
    context_object_name = "사람키"
    def get_success_url(self):
        return reverse("homepage:List")

def SaleUpdate(request,pk):
   회원 = Sale.objects.get(id=pk)  
  
   폼 = SaleModelForm(instance=회원)
   if request.method == "POST":

        폼 = SaleModelForm(request.POST,instance=회원)
        if 폼.is_valid():

           폼.save()

           return redirect("/homepage")
    
   context = {
        "폼키"   : 폼,
        "사람키" : 회원
    }
   return render(request,"folder/saleupdate.html",context)

class SaleDeleteView(generic.DeleteView):
    template_name = "folder/saledelete.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"
    def get_success_url(self):
        return reverse ("homepage:List")
    

def SaleDelete(request,pk):
  회원 = Sale.objects.get(id=pk)
  회원.delete(
  ) 
  return redirect("/homepage") 



""" def SaleUpdate(request,pk):
   회원 = Sale.objects.get(id=pk)  
  
   폼 = SaleForm()
   if request.method == "POST":

        폼 = SaleForm(request.POST)
        if 폼.is_valid():

            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            회원.first_name = first_name
            회원.last_name = last_name
            회원.age = age
            회원.save()

            return redirect("/index")
    
   context = {
        "폼키"   : 폼,
        "사람키" : 회원
    }
   return render(request,"folder/saleupdate.html",context)
 """


""" def SaleInput(request):
    폼 = SaleForm()
    if request.method == "POST":
        print("THIS IS POST METHOD")
        폼 = SaleForm(request.POST)
        if 폼.is_valid():
            print("VALID")
            print(폼.cleaned_data)
            first_name = 폼.cleaned_data['first_name']
            last_name = 폼.cleaned_data['last_name']
            age = 폼.cleaned_data['age']
            person = Person.objects.first()

            Sale.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                person = person
            )

            print("Input Sale Clear")

            return redirect("/index")
    context = {
        "폼키" : 폼

    }
    return render(request,"folder/saleinput.html",context) """


