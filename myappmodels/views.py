from django.shortcuts import render, redirect
from myappmodels.forms import BookModelForm,RegistrationForm,LoginForm
from django.views.generic import View
from myappmodels.models import Books
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

@method_decorator(signin_required,name="dispatch")
class BooksCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"book has been created")
            # Books.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"book_add.html",{"form":form})
        else:
            messages.error(request,"failed to create employee")
            return render(request,"book_add.html",{"form":form})
        
@method_decorator(signin_required,name="dispatch")
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        genre=Books.objects.all().values_list("genre",flat=True).distinct()
        print(genre)
        if "genre" in request.GET:
             gen=request.GET.get("genre")
             qs=qs.filter(genre__iexact=gen)
        return render(request,"book_list.html",{"data":qs,"genre":genre})
    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Books.objects.filter(name__icontains=name)
        return render(request,"book_list.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_details.html",{"data":qs})


@method_decorator(signin_required,name="dispatch")
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return redirect("book-all")


@method_decorator(signin_required,name="dispatch")
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"book has been changed")
            return redirect("book-details",pk=id)
        else:
            messages.error(request,"failed to change book")
            return render(request,"book_edit.html",{"form":form})


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"created")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"failed")
            return render(request,"register.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
          form=LoginForm(request.POST)
          if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(user_name,pwd)
            user_obj=authenticate(request,username=user_name,password=pwd)
            if user_obj:
                 print("valid")
                 login(request,user_obj)
                 return redirect("book-all")
            messages.error(request,"invalid credential")
            return render(request,"login.html",{"form":form})
          
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
     def get(self,request,*args,**kwargs):
          logout(request)
          return redirect("signin")
     