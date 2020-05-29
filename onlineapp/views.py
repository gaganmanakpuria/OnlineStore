from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import Persons
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"index.html")


def register(request):
    
    if request.method=="POST":
        em=request.POST['emaillogin']
        us=request.POST['usernamelogin']
        ps = request.POST['passwordlogin']
        User = get_user_model()
        user = User.objects.create_user(em,us,ps)
        user.save()
    return render(request,"registration.html")

def suplier_register(request):
    
    if request.method=="POST":
        fn=request.POST['firstnamesel']
        ln=request.POST['lastnamesel']
        em=request.POST['emailsel']
        us=request.POST['usernamesel']
        ps = request.POST['passwordsel']
        phnnum= request.POST['phonenumbersel']
        mobilenum= request.POST['Mobilenumbersel']
        Dob=request.POST['dateofbirthsel']
        maritalstatus=request.POST['maritalstatussel']
        gen= request.POST['gendersel']
        Supplier= request.POST['supliersel']
        crditlimit=request.POST['creditlimitsel']
        Apinc = request.POST['approximateincomesel']
        User = get_user_model()
        user = User.objects.create_staffuser(em,us,ps)
        user.firstname=fn
        user.save()
        user=User.objects.get(username=us)
        a=user(firstname=fn,lastname=ln,supplier=Supplier,credit_limit=crditlimit,approximate_income=Apinc,gender=gen,marital_status_code=maritalstatus,date_of_birth=Dob,mobile_phone_number=mobilenum,phone_number=phnnum)
        a.save()
         
    return render(request,"suplier_regis.html")

def loginus(request):
    if request.method=="POST":
        em=request.POST['emaillogin']
        ps = request.POST['passwordlogin']
        user = authenticate(email=em, password=ps) 
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin_dashboard")
            else:
                res = HttpResponseRedirect('/cust_dashboard')
                # if "rememberme" in r.POST:
                #     res.set_cookie("user_id",user.id)
                #     res.set_cookie("date_login",datetime.now())
                return res
            
            # if user.is_staff:
            #     return HttpResponseRedirect('/sel_dashboard')

            # if user.is_active:

            #     return HttpResponseRedirect('/cust_dashboard')
        else:
            return render(request,"index.html")
    return render(request,"login.html")

def cust_dashboard(request):
    return render(request,"cust_dashboard.html")

def admin_dashboard(request):
    context={}
    
    User= get_user_model()
    Alluser = User.objects.all()
    context['all'] =Alluser
    user=User.objects.filter(is_staff=False,is_active=False)
    context['user'] =user
    if request.method=="POST":
        if 'approve' in request.POST:
            sidd =request.POST['ssid']
            user=User.objects.get(id=sidd)
            user.is_staff=True
            user.is_active=True
            user.save()
        if 'cancel' in request.POST:
            sidd =request.POST['ssid']
            user=User.objects.get(id=sidd)
            user.save()

    return render(request,"admin/tables.html",context)
# def g(r):
#     User= get_user_model()
#     user=User.objects.filter(is_staff=False,is_active=False)
#     context['user'] =user
#     if request.method=="GET":
#         sidd =request.GET['ssid']
#         print(sidd)
#         user=User.objects.get(id=sidd)
#         print(user)

def contactus(request):
    return render(request,"contact.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render(request,"checkout.html")
def shopgrid(request):
    return render(request,"shop-grid.html")
def blog(request):
    return render(request,"blog-single-sidebar.html")


    