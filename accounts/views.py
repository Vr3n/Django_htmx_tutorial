from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

        # If the url consists of 'next' param.
        # redirect to the next="url".

        if request.GET.get('next'):
            next_url = request.GET.get('next')
            return redirect(next_url)

        # redirect to home page.
        return redirect('/')

    # Return for get request.
    return render(request, "accounts/login.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/accounts/login/')
    return render(request, "accounts/logout.html", {})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {"form": form}
    return render(request, "accounts/register.html", context)
