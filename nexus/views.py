from django.shortcuts import render,HttpResponse
from datetime import datetime
from nexus.models import Register
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')
    
    #return HttpResponse("This is Homepage")

def projects(request):
    return render(request,'projects.html')

def register(request):

    if request.method == "POST" :
        try:
            name=request.POST.get("name")
            srn=request.POST.get("srn")
            prn=request.POST.get("prn")
            email=request.POST.get("email")
            reason=request.POST.get("reason")
            print(f"Received data: name={name}, srn={srn},prn={prn}, email={email}, reason={reason}")


            Register.objects.create(name=name,srn=srn,prn=prn,email=email,reason=reason,date=datetime.today())

            messages.success(request,"Your entry has been submitted...")
        except Exception as e :
            messages.error(request, "There was an error submitting your entry.")
            print(f"Error: {e}")    
    
    return render(request,'register.html')