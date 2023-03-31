from django.shortcuts import redirect, render
from Registration.models import Register
from django.contrib import messages
import smtplib
from email.message import EmailMessage
from Registration import get_mails
from chat.models import Room, RoomMore
from datetime import time, date
from serpapi import GoogleSearch

# Home Page url
def index(request):
   return render(request, 'homepage/index.html')


# Login Registration
def login(request):
   if request.method == "POST":
      if request.POST.get("submit") == "Sign Up":
         request.session['name'] = request.POST.get("name")
         request.session['email'] = request.POST.get("email")
         request.session['password'] = request.POST.get("password")
         request.session['role'] = request.POST.get("role")
         
         reg = Register.objects.filter(email=request.session['email']).exists() 
         if reg != True:
            return redirect('emails')
         else:
            messages.error(request, "Email Already Exists")
            return render(request, 'registration/login.html')

      else:
         try:
            request.session['email'] = request.POST.get("email")
            request.session['password'] = request.POST.get("password")
            reg = Register.objects.get(email=request.session['email'],password=request.session['password'])
            request.session['id'] = reg.id
            request.session['name'] = reg.name
            request.session['loggedin'] = True
            request.session['role'] = reg.role 
            return redirect('profile')
         except Exception as e:
            print(e)
            messages.success(request, "Invalid Credentials")  
            return render(request, 'registration/login.html')
   return render(request, 'registration/login.html')

# Email Sending
def emails(request):
    msg = EmailMessage()
    msg['Subject'] = 'Verification!!'
    msg['From'] = "atharvashirkre77@gmail.com"
    msg['To'] = request.session['email']
    msg.set_content(get_mails.get(), subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("freelancing.team.77@gmail.com", "jintvfegctwnobok")
        smtp.send_message(msg)
    return render(request, 'email.html')

# Registring after confirmation of mail
def confirm(request):  
    registers = Register(name=request.session['name'], email=request.session['email'],
                                    password=request.session['password'], role=request.session['role'])
    reg = Register.objects.filter(email=request.session['email']).exists() 
    
    if reg != True:
        registers.save()
        messages.success(request, "Success")
        return redirect('login')
    else:
        messages.error(request, "Email Already Exists")
        return render(request, 'login.html')

# Profile landing page
def profile(request):
    if request.session['loggedin']: 
        context = {
            'email' : request.session["email"],
            'name' : request.session["name"],
            'id' : request.session['id'],
        }
        # print(request.session['role']) 
        if request.session['role'] == "org":   
            return render(request, 'organization/index.html', {'context' : context})
        else:
            return render(request, 'user/index.html', {'context' : context})
    else:
        messages.error(request, "Please Login")  
        return redirect('login')

#Jobs Page    
def jobs(request):
    params = {
    "engine": "google_jobs",
    "q": "Developer",
    "hl": "en",
    "api_key": "a18635695abead5b97d49074060406f08d79b06f447c05f0df2b998540c5b18a"
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    return render(request, 'user/jobs.html', {'results' : results["jobs_results"]})

# Specific Jobs Page
def specific_jobs(request):
    if request.method == "POST":
        q = request.POST.get("q")
        location = request.POST.get("location")
        params = {
        "engine": "google_jobs",
        "q": q,
        "location" : location,
        "hl": "en",
        "api_key": "a18635695abead5b97d49074060406f08d79b06f447c05f0df2b998540c5b18a"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        return render(request, 'user/specific_jobs.html', {'results' : results["jobs_results"], "q" : q})
    
# Hiring page for all types of hirings
def hire(request):
    return render(request, 'organization/hire.html')

# Auctions page 
def auction(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        password = request.POST.get("password")
        day_start = request.POST.get("day_start")
        month_start = request.POST.get("month_start")
        year_start = request.POST.get("year_start")
        day_end = request.POST.get("day_end")
        month_end = request.POST.get("month_end")
        year_end = request.POST.get("year_end")
        hr_start = request.POST.get("hr_start")
        mm_start = request.POST.get("mm_start")
        ss_start = request.POST.get("ss_start")
        hr_end = request.POST.get("hr_end")
        mm_end = request.POST.get("mm_end")
        ss_end = request.POST.get("ss_end")
        
        room = Room(name=name, owner=request.session['name']    )
        room.save()
        ts = time(int(hr_start), int(mm_start), int(ss_start))
        te = time(int(hr_end), int(mm_end), int(ss_end))
        ds = date(int(year_start), int(month_start), int(day_start))
        de = date(int(year_end), int(month_end), int(day_end))
        room_more = RoomMore(name=name, start_time=ts, end_time=te, start_date=ds, end_date=de, winner_name="NA", winner_amount="9999999", owner=request.session['name'])
        room_more.save()
        messages.success(request, "Auction added")
        return redirect("profile")
    return render(request, 'organization/auction.html')