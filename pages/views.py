from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    context = {
        'title':"Home Page",

    }
    if request.user.is_authenticated:
        context["premium"]="yeah"
    return render(request,"pages/home_page.html", context)

def about_page(request):
    context = {
        'title':"About Page"
    }
    return render(request,"pages/home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title':"Contact Page",
        'contact_form':contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request,"pages/contact_page.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Error")

    return render(request,"pages/login.html", context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username, email, password)
        return redirect("login")
    return render(request,"pages/register.html", context)