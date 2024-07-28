from django.shortcuts import render
from.models import *


# Create your views here.
def home(request):
    cdata=category.objects.all()

    return render(request,'user/index.html',{"data":cdata})

def about(request):
    return render(request,'user/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Contact=request.POST.get("contact","")
        Email = request.POST.get("email", "")
        Address=request.POST.get("address","")
        Message=request.POST.get("message","")
        x=contact(name=Name,contact=Contact,email=Email,address=Address,message=Message)
        x.save()
        status=True
    return render(request,'user/contactus.html',{'S':status})

def placement(request):
    cdata=courses.objects.all().order_by('-id')
    a=request.GET.get('msg')
    pdata=""
    if a is None:
        pdata=placements.objects.all()
    else:
        pdata=placements.objects.filter(pcourse=a)


    return render(request,'user/placement.html',{"course":cdata,"placement":pdata})

def adminlogin(request):
    return render(request,'user/adminlogin.html')

def course(request):
    return render(request,'user/courses.html')

def recuiter(request):
    return render(request,'user/recuiters.html')

def registration(request):

    if request.method=='POST':
        Name=request.POST.get("name", "")
        Mobile=request.POST.get("mobile", "")
        Email=request.POST.get("email", "")
        Password=request.POST.get("password", "")
        Address=request.POST.get("address", "")
        picname=request.FILES['fu']
        registration(name=Name,mobile=Mobile,email=Email,password=Password,address=Address,ppic=picname).save()
        return render(request,'user/registration.html')

def imagegallery(request):
    gdata=gallery.objects.all().order_by('-id')
    #gdata=gallery.objects.all().filter(branch="civil engineering",id=1)
    print(gdata)
    mydict={"d":gdata}
    return render(request,'user/gallery.html',mydict)

def course(request):
    cdata=courses.objects.all()
    print(cdata)
    mydict={"d":cdata}
    return render(request,'user/courses.html',mydict)

def recuiter(request):
    rdata=recuiters.objects.all()
    print(rdata)
    mydict={"d":rdata}
    return render(request,'user/recuiters.html',mydict)

def faculty(request):
    return render(request,'user/faculty.html')

