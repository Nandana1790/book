from django import forms
from myappmodels.models import Books
from django.contrib.auth.models import User

class BooksForm(forms.Form):
    name=forms.CharField()
    price=forms.IntegerField()
    author=forms.CharField()
    genre=forms.CharField()

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "genre":forms.TextInput(attrs={"class":"form-control"}),
            "published_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
    

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))