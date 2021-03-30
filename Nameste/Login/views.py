from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import *
from .forms import *
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


class Login(View):
    context_object_name = "user"
    template_name = "Login/login.html"

    def get(self, request):

        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        return render(request, self.template_name, {})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Register(View):
    signup = RegisterForm()

    def get(self, request):
        context = {'forms': self.signup}
        return render(request, 'Login/register.html', context)

    def post(self, request):
        forms = RegisterForm(request.POST)
        context = {'forms': self.signup}

        if forms.is_valid():
            username = forms.cleaned_data['username']
            email = forms.cleaned_data['email']
            fname = forms.cleaned_data['firstname']
            lname = forms.cleaned_data['lastname']
            address = forms.cleaned_data['address']
            streetno = forms.cleaned_data['streetno']
            postalcode = forms.cleaned_data['postalcode']
            password = forms.cleaned_data['password']
            conpassword = forms.cleaned_data['conformpassword']
            print(username, email, fname, lname, address,
                  streetno, postalcode, password, conpassword)
            try:
                get_user = User.objects.get(username=username)
                context['errors'] = '*Username is already taken*'
            except:
                if password == conpassword:
                    if len(password) > 6:
                        user = User.objects.create_user(
                            username=username, password=password, email=email, first_name=fname, last_name=lname)
                        bisteuser = Signup(fname=fname, lname=lname, email=email, username=username,
                                           address=address, streetno=streetno, postalcode=postalcode)
                        bisteuser.save()
                        Nuser = authenticate(
                            request, username=username, password=password)
                        login(request, user)

                    else:
                        context['errors'] = "*Please choose strong password*"
                else:
                    context['errors'] = "*The password isn't Long enough*"

        else:
            context['errors'] = '*Please enter a vaild email*'

        return render(request, 'Login/register.html', context)
