from django.shortcuts import redirect, render
from Registration.models import Register
from django.contrib import messages
import smtplib
from email.message import EmailMessage
from Registration import get_mails

def index(request):
    request.session['loggedin'] = False
    return render(request, 'index.html')
# @cache_page(60)
def login(request):
    if request.method == "POST":
        if request.POST.get("submit") == "Sign Up":
            request.session['name'] = request.POST.get("name")
            request.session['email'] = request.POST.get("email")
            request.session['password'] = request.POST.get("password")
            # registers = Register(name=request.session['name'], email=request.session['email'],
            #                         password=request.session['password'])
            
            reg = Register.objects.filter(email=request.session['email']).exists() 
            if reg != True:
                # registers.save()
                # reg = Register.objects.get(email=request.session['email'])
                # request.session['id'] = reg.id
                return redirect('emails')
            else:
                messages.error(request, "Email Already Exists")
                return render(request, 'login.html')

        else:
            try:
                request.session['email'] = request.POST.get("email")
                request.session['password'] = request.POST.get("password")
                reg = Register.objects.get(email=request.session['email'],password=request.session['password'])
                request.session['id'] = reg.id
                request.session['name'] = reg.name
                request.session['loggedin'] = True
                return redirect('profile')
            except Exception as e:
                # print(e)
                messages.error(request, "Invalid Credentials")  
                return render(request, 'login.html')

    return render(request, 'login.html')

def profile(request):
    if request.session['loggedin']: 
        context = {
            'email' : request.session["email"],
            'name' : request.session["name"],
            'id' : request.session['id'],
            
        }
        return render(request, 'profile.html', context)
    else:
        messages.error(request, "Please Login")  
        return redirect('login')

def emails(request):
    # print(request.session['email'])
    msg = EmailMessage()
    msg['Subject'] = 'Verification!!'
    msg['From'] = "atharvashirkre77@gmail.com"
    msg['To'] = request.session['email']
    # file = open('templates/login.html')
    # template = file.read()
    msg.set_content(get_mails.get(), subtype='html')



    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("atharvashirkre77@gmail.com", "hcceimvbxjxxdjwx")
        smtp.send_message(msg)
    return render(request, 'email.html')


def confirm(request):  
    # print(request.session['email'])
    registers = Register(name=request.session['name'], email=request.session['email'],
                                    password=request.session['password'])

    # registers.save()
    reg = Register.objects.filter(email=request.session['email']).exists() 
    
    if reg != True:
        registers.save()
        # reg = Register.objects.get(email=request.session['email'])
        # request.session['id'] = reg.id
        messages.error(request, "Success")
        return redirect('login')
    else:
        messages.error(request, "Email Already Exists")
        return render(request, 'login.html')
    
