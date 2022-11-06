from django.shortcuts import redirect, render
from Registration.models import Register
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator


def index(request):
    return render(request, 'index.html')
@cache_page(60)
def login(request):
    
    if request.method == "POST":
        if request.POST.get("submit") == "Sign Up":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            registers = Register(name=name, email=email,
                                    password=password)
            
            reg = Register.objects.filter(email=email).exists()
            if reg != True:
                registers.save()
                return render(request, 'login/login.html')
            else:
                messages.error(request, "Email Already Exists")
                return render(request, 'login/login.html')

        else:
            try:
                email = request.POST.get("email")
                password = request.POST.get("password")
                reg = Register.objects.get(email=email,password=password)
                return render(request, 'login/login.html')
            except Exception as e:
                messages.error(request, "Invalid Credentials")  
                return render(request, 'login/login.html')

    return render(request, 'login/login.html')