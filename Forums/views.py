from django.shortcuts import redirect, render

# Home Pafe of Forums
def index(request):
   return render(request, 'forums/index.html')

